import time
import board
import busio
import adafruit_bme680

# Create the I2C connection using the STEMMA QT connector (SCL and SDA pins)
i2c = busio.I2C(board.SCL, board.SDA)

# Create the BME680 sensor object
sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)

# Optional: Change the oversampling for temperature, humidity, pressure, or filter size
sensor.temperature_oversample = 8
sensor.humidity_oversample = 2
sensor.pressure_oversample = 4
sensor.filter_size = 3

# Set sea level pressure (adjust this for your location)
sensor.sea_level_pressure = 1013.25  # in hPa

# Main loop to print readings
while True:
    # Read temperature, gas resistance, humidity, pressure, and altitude
    temperature_c = sensor.temperature
    gas = sensor.gas
    humidity = sensor.humidity
    pressure_hPa = sensor.pressure
    altitude_m = sensor.altitude

    # Convert temperature to Fahrenheit
    temperature_f = temperature_c * 9 / 5 + 32

    # Convert pressure to PSI
    pressure_psi = pressure_hPa * 0.0145038

    # Print the sensor readings
    print(f"Temperature: {temperature_f:.2f} F")
    print(f"Gas: {gas} ohms")
    print(f"Humidity: {humidity:.2f} %")
    print(f"Pressure: {pressure_psi:.2f} PSI")
    print(f"Altitude: {altitude_m:.2f} meters")
    print("-----------------------------")

    # Wait before the next reading
    time.sleep(2)
