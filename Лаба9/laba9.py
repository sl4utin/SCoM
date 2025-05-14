import numpy as np
from math import *


def entropy(mas):
    if len(mas) == 0:
        return 0

    blue_count = mas.count(0)
    yellow_count = mas.count(1)
    red_count = mas.count(2)
    total = len(mas)

    blue_entropy = -(blue_count / total) * log2(blue_count / total) if blue_count else 0
    yellow_entropy = -(yellow_count / total) * log2(yellow_count / total) if yellow_count else 0
    red_entropy = -(red_count / total) * log2(red_count / total) if red_count else 0

    return blue_entropy + yellow_entropy + red_entropy


def jin(mas):
    if len(mas) == 0:
        return 0

    return 1 - ((mas.count(0) / len(mas)) ** 2 + (mas.count(1) / len(mas)) ** 2 + (mas.count(2) / len(mas)) ** 2)


# Красный - 2
# Желтый - 1
# Синий  - 0
balls = [2, 0, 1, 1, 0, 0, 0, 1, 2, 2, 2, 0, 0, 1, 1, 1, 2, 0, 2, 2]

entropyStandart = entropy(balls)
jinStandart = jin(balls)

print('Стандартные значения')
print('Энтропия', entropyStandart)
print('Индекс Джини', jinStandart)

bestForJin3 = 1
bestForJinEntropy3 = 1
bestLeftMasJin3 = []
bestCenterMasJin3 = []
bestRightMasJin3 = []

for i in range(1, len(balls) - 1):
    for j in range(i + 1, len(balls)):
        leftContainer = balls[:i]
        centerContainer = balls[i:j]
        rightContainer = balls[j:]

        weightedJin = ((len(leftContainer) / len(balls)) * jin(leftContainer) +
                       (len(centerContainer) / len(balls)) * jin(centerContainer) +
                       (len(rightContainer) / len(balls)) * jin(rightContainer))

        weightedEntropy = ((len(leftContainer) / len(balls)) * entropy(leftContainer) +
                           (len(centerContainer) / len(balls)) * entropy(centerContainer) +
                           (len(rightContainer) / len(balls)) * entropy(rightContainer))

        if weightedJin < bestForJin3:
            bestForJin3 = weightedJin
            bestForJinEntropy3 = weightedEntropy
            bestLeftMasJin3 = leftContainer
            bestCenterMasJin3 = centerContainer
            bestRightMasJin3 = rightContainer

print('\nЛучшие значения для разбиения на 3 части:')

print('\nЛучшие значения для индекса Джини:')
print('Энтропия:', bestForJinEntropy3)
print('Индекс Джини:', bestForJin3)
print(f'Левый массив ({len(bestLeftMasJin3)} элементов):', bestLeftMasJin3)
print(f'Центральный массив ({len(bestCenterMasJin3)} элементов):', bestCenterMasJin3)
print(f'Правый массив ({len(bestRightMasJin3)} элементов):', bestRightMasJin3)
print('Разница Энтропии:', abs(bestForJinEntropy3 - entropyStandart))
print('Разница индекса Джини:', abs(bestForJin3 - jinStandart))