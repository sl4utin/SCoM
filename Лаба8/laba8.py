import numpy as np
from math import *


def entropy(mas):
    if len(mas) == 0:
        return 0

    blue_count = mas.count(0)
    yellow_count = mas.count(1)
    total = len(mas)

    blue_entropy = -(blue_count / total) * log2(blue_count / total) if blue_count else 0
    yellow_entropy = -(yellow_count / total) * log2(yellow_count / total) if yellow_count else 0

    return blue_entropy + yellow_entropy


def jin(mas):
    if len(mas) == 0:
        return 0

    return 1 - ((mas.count(0) / len(mas)) ** 2 + (mas.count(1) / len(mas)) ** 2)


# Желтый - 1
# Синий  - 0
balls = [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0]

entropyStandart = entropy(balls)
jinStandart = jin(balls)

print('Стандартные значения')
print('Энтропия', entropyStandart)
print('Индекс Джини', jinStandart)

bestForJin2 = 1
bestForJinEntropy2 = 1
bestLeftMasJin2 = []
bestRightMasJin2 = []


bestForEntropy2 = 1
bestForEntropyJin2 = 1
bestLeftMasEntropy2= []
bestRightMasEntropy2 = []

for n in range (1, len(balls)):
    leftContainer = balls[:n]
    rightContainer = balls[n:]

    weightedJin = (len(leftContainer) / len(balls)) * jin(leftContainer) + (len(rightContainer) / len(balls)) * jin(rightContainer)
    weightedEntropy = (len(leftContainer) / len(balls)) * entropy(leftContainer) + (len(rightContainer) / len(balls)) * entropy(rightContainer)

    # Находим лучшее разбиение по Джини
    if weightedJin < bestForJin2:
        bestForJin2 = weightedJin
        bestForJinEntropy2 = weightedEntropy
        bestLeftMasJin2 = leftContainer
        bestRightMasJin2 = rightContainer

    # Находим лучшее разбиение по Энтропии
    if weightedEntropy < bestForEntropy2:
        bestForEntropy2 = weightedEntropy
        bestForEntropyJin2 = weightedJin
        bestLeftMasEntropy2 = leftContainer
        bestRightMasEntropy2 = rightContainer

print('\nЛучшие значения для разбиения на 2 части:')

print('\nЛучшие значения для индекса Джини')
print('Энтропия:', bestForJinEntropy2)
print('Индекс Джини:', bestForJin2)
print(f'Левый массив ({len(bestLeftMasJin2)} элементов):', bestLeftMasJin2)
print(f'Правый массив ({len(bestRightMasJin2)} элементов):', bestRightMasJin2)
print('Разница Энтропии:', abs(bestForJinEntropy2 - entropyStandart))
print('Разница индекса Джини:', abs(bestForJin2 - jinStandart))

print('\nЛучшие значения для Энтропии')
print('Энтропия:', bestForEntropy2)
print('Индекс Джини:', bestForEntropyJin2)
print(f'Левый массив ({len(bestLeftMasEntropy2)} элементов):', bestLeftMasEntropy2)
print(f'Правый массив ({len(bestRightMasEntropy2)} элементов):', bestRightMasEntropy2)
print('Разница Энтропии:', abs(bestForEntropy2 - entropyStandart))
print('Разница индекса Джини:', abs(bestForEntropyJin2 - jinStandart))

bestForJin3 = 1
bestForJinEntropy3 = 1
bestLeftMasJin3 = []
bestCenterMasJin3 = []
bestRightMasJin3 = []


bestForEntropy3 = 1
bestForEntropyJin3 = 1
bestLeftMasEntropy3= []
bestCenterMasEntropy3= []
bestRightMasEntropy3 = []

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

        if weightedEntropy < bestForEntropy3:
            bestForEntropy3 = weightedEntropy
            bestForEntropyJin3 = weightedJin
            bestLeftMasEntropy3 = leftContainer
            bestCenterMasEntropy3 = centerContainer
            bestRightMasEntropy3 = rightContainer

print('\nЛучшие значения для разбиения на 3 части:')

print('\nЛучшие значения для индекса Джини:')
print('Энтропия:', bestForJinEntropy3)
print('Индекс Джини:', bestForJin3)
print(f'Левый массив ({len(bestLeftMasJin3)} элементов):', bestLeftMasJin3)
print(f'Центральный массив ({len(bestCenterMasJin3)} элементов):', bestCenterMasJin3)
print(f'Правый массив ({len(bestRightMasJin3)} элементов):', bestRightMasJin3)
print('Разница Энтропии:', abs(bestForJinEntropy3 - entropyStandart))
print('Разница индекса Джини:', abs(bestForJin3 - jinStandart))

print('\nЛучшие значения для Энтропии:')
print('Энтропия:', bestForEntropy3)
print('Индекс Джини:', bestForEntropyJin3)
print(f'Левый массив ({len(bestLeftMasEntropy3)} элементов):', bestLeftMasEntropy3)
print(f'Центральный массив ({len(bestCenterMasEntropy3)} элементов):', bestCenterMasEntropy3)
print(f'Правый массив ({len(bestRightMasEntropy3)} элементов):', bestRightMasEntropy3)
print('Разница Энтропии:', abs(bestForEntropy3 - entropyStandart))
print('Разница индекса Джини:', abs(bestForEntropyJin3 - jinStandart))

