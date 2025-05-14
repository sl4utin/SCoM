import numpy as np
import matplotlib.pyplot as plt
from math import sin, sqrt, exp, pi


def ksi(a, tau, t):
    return (1 / sqrt(a)) * (1 - ((t - tau) / a) ** 2) * exp(-0.5 * (((t - tau) / a) ** 2))


def st(t):
    w = 2 * pi / 50
    A = 1
    u = 0
    return A * sin(w * t + u)
    # return A * sin(w * t + u) + sin(pi * t)
    # return A * sin(w * t + u) + 5 * sin(0.5 * pi * t)


def Watau(a, tau, t):
    return ksi(a, tau, t) * st(t)



a_values = np.linspace(1, 30, 30)
tau_values = np.linspace(0, 50, 50)
t_values = np.linspace(-25, 75, 1000)

A_mesh, Tau_mesh = np.meshgrid(a_values, tau_values)
Z_mesh = np.zeros_like(A_mesh)

for i in range(len(a_values)):
    for j in range(len(tau_values)):
        a = a_values[i]
        tau = tau_values[j]

        W_values = np.array([Watau(a, tau, t) for t in t_values])

        integral = np.trapz(W_values, t_values)
        Z_mesh[j, i] = integral

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(A_mesh, Tau_mesh, Z_mesh, cmap='viridis')

ax.set_xlabel('a')
ax.set_ylabel('tau')
ax.set_zlabel('Интеграл of Watau')
ax.set_title('')

plt.show()
