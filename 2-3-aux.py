import time

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

number = [0]*8

leds = [0]*8
leds[0]=2
leds[1]=3
leds[2]=4
leds[3]=17
leds[4]=27
leds[5]=22
leds[6]=10
leds[7]=9

leds= leds[::-1]

aux=[21,20,26,16,19,25,23,24]
GPIO.setup(leds, GPIO.OUT)


GPIO.setup(aux, GPIO.IN)
GPIO.output(leds,GPIO.LOW)
while 1==1:
    for i in range(8):
        GPIO.output(leds[i],GPIO.input(aux[i]))

GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)

GPIO.output(leds,GPIO.LOW)
