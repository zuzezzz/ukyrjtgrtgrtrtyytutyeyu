import numpy as np
import matplotlib.pyplot as plt
# import pandas as pd

p = np.loadtxt('/home/b04-307/Desktop/Scripts/settings.txt', dtype = float)
d = np.loadtxt('/home/b04-307/Desktop/Scripts/data.txt', dtype = int)
x = np.arange(0, len(d) / p[0], 1/p[0])
y = []
q = np.array(d)
for elem in q:
    elem = elem * p[1]
    y.append(elem)


plt.figure(figsize=(12, 16))
plt.title('Процесс заряда конденсатора в RC-цепочке')
plt.plot(x, y, color = 'green', marker = '.', linewidth = 0.8)
plt.xlabel('Время, с')
plt.ylabel('Напряжение, В')
plt.minorticks_on()
plt.grid(axis='both', color='silver', which='major')
plt.grid(axis='both', color='#F5F5F5', which='minor')
plt.xlim(0 , max(x))
plt.ylim(min(y), max(y)*1.3)
s = 'Время зарядки ' + str(round(max(x), 2)) + ' с'
plt.text(6, 2, s, backgroundcolor = 'w')
plt.savefig('/home/b04-307/Desktop/Scripts/querw.svg')

plt.show()
