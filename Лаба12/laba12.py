from math import *

def distanceMinkovskiy(people1, people2, p):
    distance = 0
    # distance =
    for i in range(4):
        distance += pow(abs(people1[i + 1] - people2[i + 1]), p)
    return pow(distance, 1 / p)

# 1 столбец - номер
# 2 столбец - возраст
# 3 столбец - зарплата в т.р.
# 4 столбец - кол-во детей
# 5 столбец - цена собственности в млн.р.
# 6 столбец - если 0, то возврат вовремя, если 1, то просрочка кредита
train = [
    [1, 46, 50, 2, 2.0, 0],
    [2, 36, 42, 2, 1.5, 0],
    [3, 34, 40, 3, 1.4, 0],
    [4, 28, 45, 1, 0.5, 1],
    [5, 24, 30, 0, 0.3, 1],
    [6, 21, 25, 0, 0.1, 1],
    [7, 35, 40, 1, 0.5, 0],
    [8, 48, 45, 2, 0.35, 0],
    [9, 35, 40, 2, 0.4, 1],
    [10, 37, 54, 2, 0.45, 0],
    [11, 18, 25, 0, 5.0, 1],
    [12, 24, 30, 1, 0.4, 1],
    [13, 33, 45, 2, 3.0, 0],
    [14, 45, 50, 1, 4.0, 1],
]
val = [
    [15, 38, 50, 2, 2.5, 0],
    [16, 24, 25, 1, 5.0, 1],
    [17, 42, 30, 3, 4.0, 0],
    [18, 36, 47, 2, 3.0, 0],
    [19, 23, 35, 0, 1.5, 1],
    [20, 40, 45, 2, 4.5, 0],
]

test = [
    [21, 35, 30, 2, 5.0, 1],
]


def knnMinkovskiyWithoutVes(p, k, train_data, test_person):
    distances = []
    for person in train_data:
        dist = distanceMinkovskiy(test_person, person, p)
        distances.append((dist, person[5]))  # (distance, class)

    # Сортируем по расстоянию и берем k ближайших соседей
    distances.sort(key=lambda x: x[0])
    nearest_neighbors = distances[:k]

    # Считаем количество соседей, вернувших кредит вовремя
    count_0= sum(1 for neighbor in nearest_neighbors if neighbor[1] == 0)
    probability = count_0 / k

    # Вывод
    print(f"\nБезвесовой KNN")
    if(probability > 0.5):
        print(f"Кредит будет сдан вовремя")
    else:
        print(f"Кредит будет просрочен")
    print(f"Вероятность возврата кредита без задержек: {probability:.2f}")
    return 0

def knnMinkovskiyWithVesLin(p, k, train_data, test_person):
    distances = []
    for person in train_data:
        dist = distanceMinkovskiy(test_person, person, p)
        distances.append((dist, person[5]))  # (distance, class)

    # Сортируем по расстоянию и берем k ближайших соседей
    distances.sort(key=lambda x: x[0])
    nearest_neighbors = distances[:k]

    # Считаем количество соседей, вернувших кредит вовремя
    value_0= sum((k+1-i)/k for i in range(len(nearest_neighbors)) if nearest_neighbors[i][1] == 0)
    value_1= sum((k+1-i)/k for i in range(len(nearest_neighbors)) if nearest_neighbors[i][1] == 1)

    # Вывод
    print(f"\nВесовой линейный KNN")
    if(value_1 > value_0):
        print(f"Кредит будет просрочен")
    else:
        print(f"Кредит будет сдан вовремя")
    print(f"Коэффицент сдачи во время: {value_0}")
    print(f"Коэффицент просрочки: {value_1}")

    return 0

p = 2
k = 7
print(f"Степень метрики Минковского: {p}")
print(f"Количество соседей: {k}")
# Предсказание вероятности для тестового примера
probabilityWithoutVes = knnMinkovskiyWithoutVes(p, k, train + val, test[0])
probabilityWithVesLin = knnMinkovskiyWithVesLin(p, k, train + val, test[0])

