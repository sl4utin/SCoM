from math import *
import json
from tabulate import tabulate

DATA = {
    1: 6.1,
    2: 8.1,
    3: 9.0,
    4: 8.2,
    5: 7.8,
    6: 8.0,
    7: 8.2,
    8: 10.0,
    9: 11.3,
    10: 11.0,
    11: 10.2,
    12: 9.8
}

X = list(DATA.keys())
Y = list(DATA.values())
N = len(X)

X2 = [x**2 for x in X]
Y2 = [y**2 for y in Y]

DELTAS = []

A = 0
B = 0
A1 = 0
A2 = 0
B1 = 0
B2 = 0

DELTA_T = []
PROGNOZ = []

def y(t):
    global A, B
    return A * t + B

def a1_func(t, delta_i):
    return DELTAS[delta_i] * cos(t)

def a2_func(t, delta_i):
    return DELTAS[delta_i] * cos(t * 2)

def b1_func(t, delta_i):
    return DELTAS[delta_i] * sin(t)

def b2_func(t, delta_i):
    return DELTAS[delta_i] * sin(t * 2)

def calculate_integral(func, T: list):
    return sum([func(t * pi / 12 * 2, t_i) for t_i, t in enumerate(T)])

def delta_t(t):
    return A1 * cos(t) + B1 * sin(t) + A2 * cos(t * 2) + B2 * sin(t * 2)


def main():
    global A, B, DELTAS, A1, A2, B1, B2, DELTA_T, PROGNOZ

    # 1. Вывод исходных данных
    print("=" * 50)
    print("{:^50}".format("ИСХОДНЫЕ ДАННЫЕ"))
    print("=" * 50)

    # Таблица исходных данных
    headers = ["Месяц (t)", "Значение (Y)"]
    table_data = [[x, y] for x, y in zip(X, Y)]
    print(tabulate(table_data, headers=headers, tablefmt="grid", floatfmt=".2f"))
    print("\n")

    # 2. Расчет тренда
    print("=" * 50)
    print("{:^50}".format("РАСЧЕТ ЛИНЕЙНОГО ТРЕНДА"))
    print("=" * 50)

    x_sum = sum(X)
    y_sum = sum(Y)
    x2_sum = sum(X2)
    y2_sum = sum(Y2)

    print(f"Сумма t: {x_sum:.2f}")
    print(f"Сумма Y: {y_sum:.2f}")
    print(f"Сумма t²: {x2_sum:.2f}")
    print(f"Сумма Y²: {y2_sum:.2f}\n")

    x_avg = x_sum / N
    y_avg = y_sum / N

    print(f"Среднее t: {x_avg:.2f}")
    print(f"Среднее Y: {y_avg:.2f}\n")

    XiYi = [x * y for x, y in zip(X, Y)]
    A = (sum(XiYi) / N - x_avg * y_avg) / (x2_sum / N - x_avg ** 2)
    B = y_avg - A * x_avg

    print("Уравнение линейного тренда:")
    print(f"y(t) = {A:.4f} * t + {B:.4f}\n")

    # 3. Расчет сезонной компоненты
    print("=" * 50)
    print("{:^50}".format("РАСЧЕТ СЕЗОННОЙ КОМПОНЕНТЫ"))
    print("=" * 50)

    Yi = [y(x) for x in X]
    DELTAS = [y_act - y_pred for y_act, y_pred in zip(Y, Yi)]

    print("\nОтклонения (Y - y(t)):")
    for i, delta in enumerate(DELTAS, 1):
        print(f"Месяц {i:2d}: {delta:+.4f}")

    # Расчет коэффициентов
    A1 = 1 / pi * calculate_integral(a1_func, X)
    A2 = 1 / pi * calculate_integral(a2_func, X)
    B1 = 1 / pi * calculate_integral(b1_func, X)
    B2 = 1 / pi * calculate_integral(b2_func, X)

    print("\nКоэффициенты гармоник:")
    print(f"A₁ = {A1:.4f}")
    print(f"A₂ = {A2:.4f}")
    print(f"B₁ = {B1:.4f}")
    print(f"B₂ = {B2:.4f}")

    # 4. Прогнозирование
    print("=" * 50)
    print("{:^50}".format("ПРОГНОЗ НА 14 МЕСЯЦЕВ ВПЕРЕД"))
    print("=" * 50)

    PROGNOZ_zip = {}
    for t in range(1, N + 14 + 1):
        PROGNOZ.append(y(t) + delta_t(t - 1))  # t-1 потому что индексация с 0
        PROGNOZ_zip[t] = y(t) + delta_t(t - 1)

    # Вывод прогноза в виде таблицы
    print("\nПрогнозные значения:")
    headers = ["Месяц", "Тренд", "Сезонная компонента", "Прогноз"]
    table_data = []
    for t in range(1, N + 14 + 1):
        trend = y(t)
        seasonal = delta_t(t - 1)
        forecast = trend + seasonal
        table_data.append([t, f"{trend:.2f}", f"{seasonal:+.2f}", f"{forecast:.2f}"])

    # Выводим первые 12 месяцев и затем прогноз
    print("\nИсходный период (12 месяцев):")
    print(tabulate(table_data[:12], headers=headers, tablefmt="grid", floatfmt=".2f"))

    print("\nПрогноз на следующие 14 месяцев:")
    print(tabulate(table_data[12:], headers=headers, tablefmt="grid", floatfmt=".2f"))

    # Сохранение в JSON для возможного использования
    with open("forecast_results.json", "w") as f:
        json.dump({
            "trend_equation": f"y(t) = {A:.4f} * t + {B:.4f}",
            "harmonic_coefficients": {
                "A1": A1,
                "A2": A2,
                "B1": B1,
                "B2": B2
            },
            "forecast": PROGNOZ_zip
        }, f, indent=4)


main()