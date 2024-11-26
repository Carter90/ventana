import time
import board
import busio
from adafruit_mpu6050 import MPU6050

# Initialize I2C bus and the MPU-6050 sensor
i2c = busio.I2C(board.SCL, board.SDA)
mpu = MPU6050(i2c)

try:
    while True:
        # Read accelerometer values
        accel_x, accel_y, accel_z = mpu.acceleration
        # Read gyroscope values
        gyro_x, gyro_y, gyro_z = mpu.gyro
        # Read temperature in Celsius
        temperature = mpu.temperature

        # Print the readings
        print(f"Acceleration (m/s^2): X={accel_x:.2f}, Y={accel_y:.2f}, Z={accel_z:.2f}")
        print(f"Gyroscope (degrees/s): X={gyro_x:.2f}, Y={gyro_y:.2f}, Z={gyro_z:.2f}")
        print(f"Temperature (°C): {temperature:.2f}")
        print("-" * 40)

        # Delay before the next reading
        time.sleep(1)

except KeyboardInterrupt:
    print("Program stopped by User.")
