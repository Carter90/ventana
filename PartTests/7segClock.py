import time
import board
from adafruit_ht16k33.segments import Seg7x4
from datetime import datetime

# Initialize the I2C interface and display
i2c = board.I2C()
display = Seg7x4(i2c)

# Function to update the display with the current time in 12-hour format
def update_time():
    now = datetime.now()
    current_time = now.strftime("%I:%M")  # Format the time as 12-hour (HH:MM)
    display.print(current_time)  # Update the display
    display.show()  # Refresh the display

# Main loop to keep updating the time every second
while True:
    update_time()
    time.sleep(1)  # Wait for 1 second before updating again

