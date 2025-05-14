
x = [1, 2, 3, 4, 5]
y = [1, 2, 9, 10, 10]

rss = 100
leftContainerBest = []
centerContainerBest = []
rightContainerBest = []

for i in range(1, len(y) - 1):
    for j in range(i + 1, len(y)):
        leftContainer = y[:i]
        centerContainer = y[i:j]
        rightContainer = y[j:]

        rssContainer = [0] * 3

        for i in range(len(leftContainer)):
            rssContainer[0] += (leftContainer[i] - sum(leftContainer) / len(leftContainer)) ** 2

        for i in range(len(centerContainer)):
            rssContainer[1] += (centerContainer[i] - sum(centerContainer) / len(centerContainer)) ** 2

        for i in range(len(rightContainer)):
            rssContainer[2] += (rightContainer[i] - sum(rightContainer) / len(rightContainer)) ** 2

        if(rss > sum(rssContainer)):
            rss = sum(rssContainer)
            leftContainerBest = leftContainer
            centerContainerBest = centerContainer
            rightContainerBest = rightContainer

print(f'Минимальный RSS: {rss}')
print(f'Контейнеры:')
print(f'Левый: {leftContainerBest}')
print(f'Центральный: {centerContainerBest}')
print(f'Правый: {rightContainerBest}')