import RPi.GPIO as gpio
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

# decimal to binary
def d2b(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    value, b = 0, 0
    period = float(input('Enter period: '))
    while True:
        gpio.output(dac, d2b(value))
        if value == 0:
            b = 1
        if value == 255:
            b = 0
        if b == 1:
            value += 1
        else:
            value -= 1

        time.sleep(period / 512)

except ValueError:
    print('Enter valid period')
    
finally:
    gpio.output(dac, 0)
    gpio.cleanup()