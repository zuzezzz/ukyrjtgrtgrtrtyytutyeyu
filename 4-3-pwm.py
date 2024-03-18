import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup([21, 9], gpio.OUT)
p = gpio.PWM(21, 1000)
p.start(0)
p1 = gpio.PWM(9, 1000)
p1.start(0)
try: 
    while True:
        a = float(input('Enter duty cycle: '))
        p.ChangeDutyCycle(a)
        p1.ChangeDutyCycle(a)
        print(round(3.3 / 100 * a, 2))
except ValueError:
    print('Enter valid value: ')

finally:
    p.stop()
    gpio.output([21, 9], 0)
    gpio.cleanup()
