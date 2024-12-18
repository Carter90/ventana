# VAS(Ventana Automation System) for a Gulfstar 37 Sailboat

This system will integrate all the systems on a sailboat including propulsion, lights, sensors ect, radios. 
Details regarding the resortation of the physical boat can be found at boat.carterfrost.com

Current systems diagram *subject to change*
```mermaid
flowchart LR
MS[/Mast Sensors/] -->|ROS over Ethernet| EKF[EKF]
HS[/Helm Sensors/] -->|ROS over Ethernet| EKF[EKF]
BS[/Bow Sensors/] -->|ROS over Ethernet| EKF[EKF]
GPS[/GPS/] -->|ROS over Ethernet| EKF[EKF]
EKF[EKF] -->|ROS over localhost| Localization[Localization]
Waypoint[/External Waypoint feed/] --> MControl
Localization[Localization] --> |Local Localization| MControl
Localization[Localization] --> |Global Localization| MControl
Localization[Localization] --> |Map View| Web[Web via Flask]

throughhull[/Through-hull Sensor/] --> |ROS over Ethernet| EKF
Sonar[/Sonar Forward Array/] --> EKF
throughhull-->AControl
Sonar-->AControl

Tablet/Phone/Laptop-->|Wifi 3g & 5g| Web[Web via Flask] --> |ROS over Ethernet|MControl
Helm --> |ROS over Ethernet| MControl
MControl[Motor Control] <-->|CAN bus| Motor[/Motor/]
Web[Web via Flask] --> AControl[Auxiliary Control] --> Pumps[/Pumps/]
Helm --> AControl[Auxiliary Control] --> Lights[/Lights/]
VOSK[/VOSK Offline Speech Recognition/] --> MControl
VOSK --> AControl --> Alarms[/Alarms/]
ABilge[/Abaft Bilge Water Levels/] --> AControl
MBilge[/Mast Bilge Water Levels/] --> AControl
MS ~~~|"Mast, Helm & Bow have a IMU, accelerometer, gyroscope & magnetometers"| MS
MControl <--> |ROS Status/Alarms|AControl      

All[/All Topic's Data/] -->|ROS over Wifi, Ethernet & localhost| Logger[Logger] -->|Synced| DB[(SQLite DB)]
```

For the port/starboard portlight's I'm installing these Flexible Silicone Neon-Like LED Strips https://www.adafruit.com/product/3860  
For the main controlable lights with a set in the v-birth, head, galley & saloon  
Flexible LED Strip - 352 LEDs per meter - 1m long - Red https://www.adafruit.com/product/4846  
Ultra Flexible White LED Strip - 480 per meter - 5m long - Warm White ~3000K https://www.adafruit.com/product/4840  

Then using TIP120-R Transistors at each controllable light to run a single control line to a main computer Arduino or raspberry pi(probably will have both). Right now its just a Arduino UNO for testing. I can use it for simple on and off as well a send a PWM to pulse to effectively dim the LED strips as long as the ground is not isolated they do not strobe too bad.   

Main boat computers are 2x Raspberry Pi 4 Model B https://www.adafruit.com/product/4564  
It has GPIO breakout boards and many sensors and controls  
The main display in the cockpit is a Adafruit 2.13" Monochrome E-Ink Bonnet for Raspberry Pi - SSD1680 https://www.adafruit.com/product/4687  
This allows for clear and visible readings when underway in direct sunlight  
For nighttime for things like time and headings, depth, or any anything that is a floating point number I want displayed Adafruit 1.2" 4-Digit 7-Segment Display w/I2C Backpack - Red https://www.adafruit.com/product/1270  

A few of the starting components ie Raspberry Pi 4 Model B, IMU, Gyros, Wii Nunchuk Controller, 7segment display, paper display, rotary encoder with switches ect.  
![image](https://github.com/user-attachments/assets/a870a949-c9db-4369-a92c-a95e79bf3a6a)

Will use multiple microphones setup with a VOSK Offline Speech Recognition to run certain controls with specific keywords. 
