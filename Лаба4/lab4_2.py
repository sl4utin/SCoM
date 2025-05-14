import numpy as np
import matplotlib.pyplot as plt
from math import *

def x(t):
    A = 3
    return A * (sin(pi * t))**2

def x2(c_values, t):
    return sum(c_values[n] * h_functions[n](t) for n in range(8))

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

h_functions = [h0t, h1t, h2t, h3t, h4t, h5t, h6t, h7t]
t_values = np.linspace(0, 1, 10000)
c_values = [1.5, 0, -0.68, 0.68, -0.14, -0.14, 0.14, 0.14]

x_values = [x(t) for t in t_values]
x2_values = [x2(c_values, t) for t in t_values]
error_values = [abs(x_values[i] - x2_values[i]) for i in range(len(t_values))]

dt = t_values[1]-t_values[0]
integral_error = sum(error**2 * dt for error in error_values)
print(f"Интеграл квадрата ошибки: {integral_error}")

plt.figure(figsize=(10, 6))
plt.plot(t_values, x_values, label="x(t)", linewidth=2)
plt.plot(t_values, x2_values, label="x*(t)", linewidth=2)
plt.plot(t_values, error_values, label="error(t)", linewidth=2)
plt.xlabel("t")
plt.ylabel("Значение функции")
plt.legend()
plt.title("Графики x(t), x*(t) и error(t)")
plt.grid()

plt.show()