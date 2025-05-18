from math import *

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


def show_plot(points):
    global A_MIN, A_MAX, TAU_MIN, TAU_MAX

    func = lambda t, a, tau: s(t) * ksi(t, a, tau)
    x = []
    y = []
    z = []
    for i in points:
        for point in i:
            x.append(point[0])
            y.append(point[1])
            z.append(point[2])

    # X, Y = np.meshgrid(x, y)
    # # Z = np.array([z, [x for x in range(len(z))]])
    # Z = np.ndarray((len(X), len(Y)))
    # for x in X:
    #     for y in Y:
    #         Z[x, y] = calculate_integral(func, x, y, -15, 75)

    # Z = calculate_integral(func, X, Y, -15, 75)
    # Z = np.sqrt(X ** 2 + Y ** 2)

    # ax = fig.add_subplot(projection='3d')
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    # ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    # ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax.scatter(x, y, z)

    ax.set_xlabel('A')
    ax.set_ylabel('TAU')
    ax.set_zlabel('Z')

    fig.canvas.draw()
    plt.show()


def calculate_integral(func, a, tau, start, end):
    integral = 0
    x = start
    h = 0.5
    while x < end:
        integral += func(x, a, tau)
        x += h
    return integral


def ksi(t, a, tau):
    return (1 / sqrt(a)) * (1 - ((t - tau) / a) ** 2) * (exp((-1 / 2) * ((t - tau) / a) ** 2))


def s(t):
    global A, OMEGA1, FI, B, OMEGA2
    # return A * sin(OMEGA1 * t + FI)
    return A * sin(OMEGA1 * t + FI) + B * sin(OMEGA2 * t + FI)


A = 1
B = 0.5
FI = 0
T1 = 50
T2 = 2
OMEGA1 = 2 * pi / T1
OMEGA2 = 2 * pi / T2

A_MIN = 1
A_MAX = 30
TAU_MIN = 0
TAU_MAX = 50


def main():
    global A_MIN, A_MAX, TAU_MIN, TAU_MAX

    func = lambda t, a, tau: s(t) * ksi(t, a, tau)

    result = []
    a = A_MIN
    ha = 1
    while a < A_MAX:
        all_tau = []

        tau = TAU_MIN
        htau = ha
        while tau < TAU_MAX:
            all_tau.append([a, tau, calculate_integral(func, a, tau, -15, 75)])
            tau += htau
        result.append(all_tau)

        a += ha

    print(result)

    show_plot(result)


if __name__ == '__main__':
    main()
