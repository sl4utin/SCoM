import numpy as np
import matplotlib.pyplot as plt
from math import *
import random as rnd

def ksi(k):
    return rnd.random() * k

def y1(t):
    A = 1
    ksik = 0.1
    return A * (sin(2 * pi * t)) + ksi(ksik)

def y2(t):
    A = 1
    ksik = 0.1
    return A * (sin(2 * pi * t)) + t + ksi(ksik)

def y3(t):
    A = 1
    ksik = 0.1
    return A * (sin(pi * t)) + ksi(ksik)

def h0t(t):
    if(0 <= t < 1):
        return 1
    else:
        return 0

def h1t(t):
    if (0 <= t < 1/2):
        return 1
    elif (1/2 <= t < 1):
        return -1
    else:
        return 0

def h2t(t):
    return sqrt(2) * h1t(2*t)

def h3t(t):
    return sqrt(2) * h1t(2*t - 1)

def h4t(t):
    return 2 * h1t(4*t)

def h5t(t):
    return 2 * h1t(4*t - 1)

def h6t(t):
    return 2 * h1t(4*t - 2)

def h7t(t):
    return 2 * h1t(4*t - 3)

# h_functions = [h0t, h1t, h2t, h3t, h4t, h5t, h6t, h7t]
h_functions = [h1t, h2t, h3t, h4t, h5t, h6t, h7t]

iteration = 10000
shag = 1 / iteration

t_values = np.linspace(0, 1, iteration)


# Первый этап
c1_values = [0] * len(h_functions)
c2_values = [0] * len(h_functions)
c3_values = [0] * len(h_functions)

for t in range(len(t_values) - 1):
    for nk in range(len(h_functions)):
        c1_values[nk] += (y1(t_values[t]) * h_functions[nk](t_values[t]) + y1(t_values[t + 1]) * h_functions[nk](t_values[t + 1])) * shag / 2
        c2_values[nk] += (y2(t_values[t]) * h_functions[nk](t_values[t]) + y2(t_values[t + 1]) * h_functions[nk](t_values[t + 1])) * shag / 2
        c3_values[nk] += (y3(t_values[t]) * h_functions[nk](t_values[t]) + y3(t_values[t + 1]) * h_functions[nk](t_values[t + 1])) * shag / 2

print('c_values')
print(c1_values)
print(c2_values)
print(c3_values)

# Второй этап
c1_valuesShtrih = [0] * len(h_functions)
c2_valuesShtrih = [0] * len(h_functions)
c3_valuesShtrih = [0] * len(h_functions)

for nk in range(len(h_functions)):
    c1_valuesShtrih[nk] = c1_values[nk] / sqrt(sum(pow(c1_values[n], 2) for n in range(len(h_functions))))
    c2_valuesShtrih[nk] = c2_values[nk] / sqrt(sum(pow(c2_values[n], 2) for n in range(len(h_functions))))
    c3_valuesShtrih[nk] = c3_values[nk] / sqrt(sum(pow(c3_values[n], 2) for n in range(len(h_functions))))

print('c_valuesShtrih')
print(c1_valuesShtrih)
print(c2_valuesShtrih)
print(c3_valuesShtrih)

# Третий этап
cos = [0] * 3
cos[0] = abs(sum((c1_valuesShtrih[i] * c2_valuesShtrih[i]) for i in range(len(h_functions))))
cos[1] = abs(sum((c1_valuesShtrih[i] * c3_valuesShtrih[i]) for i in range(len(h_functions))))
cos[2] = abs(sum((c2_valuesShtrih[i] * c3_valuesShtrih[i]) for i in range(len(h_functions))))

ms = [1-cos[i] for i in range(len(cos))]

print('cos')
print(cos)

print('MS1')
print(ms)


# Графики функций y1, y2, y3
plt.plot(t_values, [y1(t) for t in t_values], label='y1(t) = sin(2πt) + E(t)')
plt.plot(t_values, [y2(t) for t in t_values], label='y2(t) = sin(2πt) + t + E(t)')
plt.plot(t_values, [y3(t) for t in t_values], label='y3(t) = sin(πt) + E(t)')
plt.title('Исходные функции')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()