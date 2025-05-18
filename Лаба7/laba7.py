import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other) -> bool:
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __hash__(self):
        return hash(f'{self.x}{self.y}')


def get_approximation_by_containers(containers: list):
    x = []
    y = []

    for container in containers:
        x.append(find_min_by_x_in_container(container).x)
        y.append(get_avg_y_in_container(container))
        x.append(find_max_by_x_in_container(container).x)
        y.append(get_avg_y_in_container(container))
    return x, y


def visualize_points(points: list[Point], containers: list):
    x = [point.x for point in points]
    y = [point.y for point in points]

    plt.plot(x, y, c='b')
    approximation_x, approximation_y = get_approximation_by_containers(containers)
    plt.plot(approximation_x, approximation_y, c='g')
    plt.show()


def calculate_container_dispersia(points: list[Point]):
    average_value = get_avg_y_in_container(points)
    return sum([(point.y - average_value)**2 for point in points]) / len(points)


def get_container_by_i(points: list[Point], i: int) -> list[Point]:
    return points[0:i]


def find_min_by_x_in_container(points: list[Point]):
    return min(points, key=lambda point: point.x)


def find_max_by_x_in_container(points: list[Point]):
    return max(points, key=lambda point: point.x)


def find_containers(points: list[Point]):
    containers = []  # list[list[Point]]

    uncontainerized_points = points.copy()

    print(f'Дисперсия - Контейнер: ')
    while len(uncontainerized_points) > 3:
        dispersias = {}  # [int, float]
        for i in range(3, len(uncontainerized_points)):
            curr_container = get_container_by_i(uncontainerized_points, i)
            dispersias[i] = calculate_container_dispersia(curr_container)

        best_i = list(dispersias.keys())[0]
        best_dispersia = list(dispersias.values())[0]
        for i, dispersia in dispersias.items():
            if dispersia < best_dispersia:
                best_i = i
                best_dispersia = dispersia

        if len(uncontainerized_points[best_i:len(uncontainerized_points)]) < 3:
            best_i = len(uncontainerized_points)

        container = get_container_by_i(uncontainerized_points, best_i)
        print(f'{best_dispersia} - {container}')
        containers.append(container)
        uncontainerized_points = uncontainerized_points[best_i:len(uncontainerized_points)]

    if len(uncontainerized_points) != 0:
        containers.append(uncontainerized_points)
        print(f'{best_dispersia} - {uncontainerized_points}')
        print('====')

    print()
    return containers


def find_container_by_x(containers: list, x: float):
    for container in containers:
        min = find_min_by_x_in_container(container).x
        max = find_max_by_x_in_container(container).x
        if min <= x <= max:
            return container
    raise Exception('Не удалось найти контейнер по x')


def get_avg_y_in_container(container: list[Point]):
    return sum([point.y for point in container]) / len(container)


def predict_y(containers: list, x: float):
    container = find_container_by_x(containers, x)
    return get_avg_y_in_container(container)


POINTS = [
    Point(1, 1.0),
    Point(2, 2.5),
    Point(3, 2.0),
    Point(4, 5.0),
    Point(5, 3.0),
    Point(6, 4.0),
    Point(7, 4.5),
    Point(8, 4.8),
    Point(9, 3.9),
    Point(10, 2.0),
    Point(11, 2.8),
    Point(12, 1.0),
    Point(13, -2.0),
    Point(14, -0.5),
    Point(15, -1.5),
    Point(16, -2.0),
    Point(17, -2.3),
    Point(18, -1.0)
]


def main():
    global POINTS

    points = POINTS.copy()
    print(points)

    containers = find_containers(points)
    containers_with_avg = {}
    for container in containers:
        containers_with_avg[get_avg_y_in_container(container)] = container
    print(containers_with_avg)

    test_points = [
        Point(4.5, predict_y(containers, 4.5)),
        Point(13.5, predict_y(containers, 13.5)),
        Point(17.2, predict_y(containers, 17.2))
    ]
    print(f'Предсказания:\n{test_points}')

    visualize_points(points, containers)


if __name__ == '__main__':
    main()

