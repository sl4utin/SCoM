import numpy as np
import matplotlib.pyplot as plt

# Настройки
width, height = 20, 10
num_centers = 6
num_points = 200

# np.random.seed(42)
centers = np.random.rand(num_centers, 2) * [width, height]
points = np.random.rand(num_points, 2) * [width, height]

def assign_points(points, centers):
    distances = np.linalg.norm(points[:, np.newaxis] - centers, axis=2)
    return np.argmin(distances, axis=1)

def update_centers(points, assignments, k):
    new_centers = np.zeros((k, 2))
    for i in range(k):
        cluster_points = points[assignments == i]
        if len(cluster_points) > 0:
            new_centers[i] = cluster_points.mean(axis=0)
        else:
            new_centers[i] = np.random.rand(2) * [width, height]
    return new_centers

assignments = assign_points(points, centers)
iteration = 1
while True:
    new_centers = update_centers(points, assignments, num_centers)
    new_assignments = assign_points(points, new_centers)

    # Печатаем изменения
    changes = []
    for idx, (old, new) in enumerate(zip(assignments, new_assignments)):
        if old != new:
            changes.append((idx, old, new))

    if not changes:
        break

    print(f"\nИтерация {iteration}:")
    for idx, old, new in changes:
        print(f"  Точка {idx} переместилась от центра {old} к центру {new}")

    centers = new_centers
    assignments = new_assignments
    iteration += 1

# Визуализация
plt.figure(figsize=(10, 5))
for i in range(num_centers):
    cluster_points = points[assignments == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], c='black', s=10)
    plt.scatter(centers[i, 0], centers[i, 1], c='red', s=100, marker='x')

    for point in cluster_points:
        plt.plot([point[0], centers[i, 0]], [point[1], centers[i, 1]], color='gray', linewidth=0.5)

plt.title('Кластеры с соединительными линиями к центрам')
plt.xlim(0, width)
plt.ylim(0, height)
plt.grid(True)
plt.show()

# Финальный вывод: точка → центр
print("\nФинальное распределение точек по центрам:")
for i in range(num_points):
    print(f"Точка {i} принадлежит центру {assignments[i]}")
