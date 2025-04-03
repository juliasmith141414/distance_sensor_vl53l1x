from machine import I2C
from machine import UART
from vl53l1x import VL53L1X
import time

uart = UART(2, 9600,tx=2,rx=4)

i2c = I2C(0)
distance = VL53L1X(i2c)
while True:
    dist_value = distance.read()  # Read the distance value
    print("range: mm ", dist_value)
    uart.write(b'AZSH9' + str(dist_value).encode() + b'YB')  # Convert distance to bytes and concatenate
    time.sleep_ms(50)

