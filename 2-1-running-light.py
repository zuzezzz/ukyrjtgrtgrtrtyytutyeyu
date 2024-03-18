import time

import RPi.GPIO as GPIO

GPIO.cleanup()
LED1=9
leds = [0]*8
leds[0]=2
leds[1]=3
leds[2]=4
leds[3]=17
leds[4]=27
leds[5]=22
leds[6]=10
leds[7]=9
GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)


GPIO.output(leds,GPIO.LOW)
for i in range (3):
    for j in range(8):
        GPIO.output(leds[j],GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(leds[j],GPIO.LOW)


GPIO.output(leds,GPIO.LOW)
GPIO.cleanup()
