import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [8, 11, 7, 1,  0,  5,  12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
troyka = 13
comp = 14

length = len(dac)
levels = 2 ** length
voltage_range = 3.3
sampling = 256

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = 0)
#GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2**i
        d = dec2bin(k)
        #print(dec2bin(k))
        GPIO.output(dac, d)
        time.sleep(0.01)
        c = GPIO.input(comp)
        if c == 1:
            k -= 2**i
    return k

#для вывода на лампы
def led(n):
    b = int(n*10/256)
    lams = [0] * 8
    for i in range(n-1):
        lams[i] = 1
        return lams

acp = []

try:
    #начало зарядки
    GPIO.setup(troyka, GPIO.OUT, initial = 1)
    start_time = time.time()
    umax = 2.7
    umin = 0.3
    x = 0
    print('The charge started')
    while 3.3 * x / 256 < umax:
        x = adc()
        acp.append(x)
        GPIO.output(leds, led(x))
    GPIO.setup(troyka, GPIO.OUT, initial = 0)
    print('The charge ended')

    #начало разрядки
    #while 3.3 * x /256 > umin:
   #     x = adc()
    #    acp.append(3.3*x/256)
     #   GPIO.output(leds, led(x))
    #print('The end of measurement')

    end_time = time.time()
    experiment_time = end_time - start_time


    with open('/home/b04-307/Desktop/Scripts/data.txt', 'w') as f:
        f.writelines(f'{item}\n' for item in acp)

    with open('/home/b04-307/Desktop/Scripts/settings.txt', 'w') as g:
        frequency = str(len(acp) / experiment_time) + '\n'
        g.write(frequency)
        quant = str(3.3 / 256)
        g.write(quant)
    print('The end')
    t = [i for i in range(len(acp))]
    print('Время эксперимента: ', experiment_time)
    print('Частота дискретизации: ', frequency)
    print('Количество измерений: ', len(acp))
    print('Шаг квантования: ', quant)

    #plt.lineplot(t, acp)
    plt.plot(t, acp)
    plt.show()

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()



        