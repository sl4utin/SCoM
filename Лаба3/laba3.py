import numpy as np
import matplotlib.pyplot as plt
from math import *

# Функция ksi
def ksi(a, tau, t):
    return (1 / sqrt(a)) * (1 - ((t - tau) / a) ** 2) * exp(-0.5 * (((t - tau) / a) ** 2))

# Функция Watau
def Watau(a, tau, t_values, f_values):
    return np.array([ksi(a, tau, t) * f for t, f in zip(t_values, f_values)])

a_values = np.linspace(0.5, 3, 25)
tau_values = np.linspace(0, 6.5, 650)

# a_values = np.linspace(3.0, 3.1, 100)
# tau_values = np.linspace(0, 10, 100)

t_values = [0, 0.5, 1, 1.6, 2.1, 2.6, 3.1, 3.4, 3.6, 3.9, 4.2, 4.45, 4.7, 4.97, 5.24, 5.5, 5.7, 6.02, 6.28]
f_values = [0, 0.5, 0.9, 0.98, 0.8, 0.4, -0.8, 1.6, -1.4, -1.6, 1, -1.4, -2, 1.1, -1.1, -2.6, 1.8, 0, -1.05]

A_mesh, Tau_mesh = np.meshgrid(a_values, tau_values)
Z_mesh = np.zeros_like(A_mesh)

for i in range(len(a_values)):
    for j in range(len(tau_values)):
        a = a_values[i]
        tau = tau_values[j]

        W_values = Watau(a, tau, t_values, f_values)
        integral = np.trapz(W_values, t_values)
        Z_mesh[j, i] = integral

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(A_mesh, Tau_mesh, Z_mesh, cmap='viridis')

ax.set_xlabel('a')
ax.set_ylabel('tau')
ax.set_zlabel('Интеграл Wataut')
ax.set_title('График интеграла Wataut')

plt.show()
