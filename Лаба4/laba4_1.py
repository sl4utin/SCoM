import numpy as np
# import matplotlib.pyplot as plt
from math import *

# Функция x(t)
def x(t):
    A=3
    return A * (sin(pi * t)) * (sin(pi * t))

def h0t(t):
    return x(t)

def h1t(t):
    if(t<1/2):
        return x(t)
    else:
        return -x(t)

def h2t(t):
    return sqrt(2)*(h1t(2*t-0))

def h3t(t):
    return sqrt(2)*(h1t(2*t-1))

def h4t(t):
    return 2*(h1t(4*t-0))

def h5t(t):
    return 2*(h1t(4*t-1))

def h6t(t):
    return 2*(h1t(4*t-2))

def h7t(t):
    return 2*(h1t(4*t-3))



t_values = np.linspace(0, 1, 10000)

c_values = [0, 0, 0, 0, 0, 0, 0, 0]

for c in range(len(t_values)):
    c_values[0]+=h0t(t_values[c])/len(t_values)
    c_values[1]+=h1t(t_values[c])/len(t_values)
    c_values[2]+=h2t(t_values[c])/len(t_values)
    c_values[3]+=h3t(t_values[c])/len(t_values)
    c_values[4]+=h4t(t_values[c])/len(t_values)
    c_values[5]+=h5t(t_values[c])/len(t_values)
    c_values[6]+=h6t(t_values[c])/len(t_values)
    c_values[7]+=h7t(t_values[c])/len(t_values)

print(c_values)