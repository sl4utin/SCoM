import numpy as np
from math import *

def y1(t):
    A = 1
    return A * (sin(2 * pi * t))

def y2(t):
    A = 1
    return A * (sin(2 * pi * t)) + t

def y3(t):
    A = 1
    return A * (sin(pi * t))

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
n_numbers = [0, 1, 1, 2, 2, 2, 2]

iteration = 10000
shag = 1 / iteration

t_values = np.linspace(0, 1, iteration)

# Первый этап
alphaY1 = [0] * len(n_numbers)
alphaY2 = [0] * len(n_numbers)
alphaY3 = [0] * len(n_numbers)

for t in range(len(t_values) - 1):
    for nk in range(len(n_numbers)):
        alphaY1[nk] += (h_functions[nk](t_values[t]) * y1(t_values[t]) + h_functions[nk](t_values[t + 1]) * y1(t_values[t + 1])) * shag / 2
        alphaY2[nk] += (h_functions[nk](t_values[t]) * y2(t_values[t]) + h_functions[nk](t_values[t + 1]) * y2(t_values[t + 1])) * shag / 2
        alphaY3[nk] += (h_functions[nk](t_values[t]) * y3(t_values[t]) + h_functions[nk](t_values[t + 1]) * y3(t_values[t + 1])) * shag / 2

print('alphaY')
print(alphaY1)
print(alphaY2)
print(alphaY3)


# Второй этап
alphaShtrih2Y1 = [0] * len(n_numbers)
alphaShtrih2Y2 = [0] * len(n_numbers)
alphaShtrih2Y3 = [0] * len(n_numbers)

for nk in range(len(n_numbers)):
    alphaShtrih2Y1[nk] = (pow(2, n_numbers[nk] / 2) * alphaY1[nk]) / (sqrt(sum((pow(alphaY1[n], 2) * pow(2, n_numbers[n])) for n in range(len(n_numbers)))))
    alphaShtrih2Y2[nk] = (pow(2, n_numbers[nk] / 2) * alphaY2[nk]) / (sqrt(sum((pow(alphaY2[n], 2) * pow(2, n_numbers[n])) for n in range(len(n_numbers)))))
    alphaShtrih2Y3[nk] = (pow(2, n_numbers[nk] / 2) * alphaY3[nk]) / (sqrt(sum((pow(alphaY3[n], 2) * pow(2, n_numbers[n])) for n in range(len(n_numbers)))))

print('alphaShtrih2Y')
print(alphaShtrih2Y1)
print(alphaShtrih2Y2)
print(alphaShtrih2Y3)

# Третий этап
cos = [0] * 3
cos[0] = abs(sum((alphaShtrih2Y1[i] * alphaShtrih2Y2[i]) for i in range(len(n_numbers))))
cos[1] = abs(sum((alphaShtrih2Y1[i] * alphaShtrih2Y3[i]) for i in range(len(n_numbers))))
cos[2] = abs(sum((alphaShtrih2Y2[i] * alphaShtrih2Y3[i]) for i in range(len(n_numbers))))

ms = [1-cos[i] for i in range(len(cos))]

print('cos')
print(cos)

print('MS1')
print(ms)
