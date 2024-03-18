import time

import RPi.GPIO as GPIO

number = [0]*8

dac = [8,11,7,1,0,5,12,6]

dac = dac[::-1]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

GPIO.output(dac,GPIO.LOW)



number[0]=1
number[2]=1
#number=[1,1,1,1,1,1,1,0]

for i in range(8):
    if number[i]==0:
        GPIO.output(dac[i],GPIO.LOW)
    else:
        GPIO.output(dac[i],GPIO.HIGH)

time.sleep(30)
GPIO.output(dac,GPIO.LOW)
GPIO.cleanup()
