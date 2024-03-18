import RPi.GPIO as gpio

dac = [8, 11, 7, 1, 0, 5, 12, 6]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

# decimal to binary
def d2b(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

# output to dac and show voltage
try:
    while True:
        number = input('Input your number: ')
        if number == 'q':
            break
        try: 
            number = int(number)
        except ValueError:
            print('You should input an integer number')
            continue
        if int(number) > 256 or int(number) < 0:
            print('This number is not lying between 0 and 256')
            continue
        answer = d2b(number)
        gpio.output(dac, answer)
        voltage = round(3.3 / 256 * number,2)
        print(voltage)


finally:
    gpio.output(dac, 0)
    gpio.cleanup()
