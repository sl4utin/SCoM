def analyze(peoples):
    ageCheck = 30
    salaryCheck = 40
    assetsCheck = 3
    kidsCheck = 1
    correct = 0

    for person in peoples:
        number, age, salary, kids, assets, overdue = person

        if age > ageCheck:
            if kids > kidsCheck:
                if salary > salaryCheck:
                    prediction = 0
                else:
                    prediction = 1
            else:
                if assets > assetsCheck:
                    prediction = 1
                else:
                    prediction = 0
        else:
            prediction = 1


        result = "✅" if prediction == overdue else "❌"
        if prediction == overdue:
            correct += 1
        print(f"Для {number}: Предсказано {prediction}, Факт {overdue} {result}")

    print(f"\nТочность: {correct}/{len(peoples)} = {correct / len(peoples) * 100:.1f}%\n\n")


train = [
    [1,  46, 50, 2, 2.0, 0],
    [2,  36, 42, 2, 1.5, 0],
    [3,  34, 40, 3, 1.4, 0],
    [4,  28, 45, 1, 0.5, 1],
    [5,  24, 30, 0, 0.3, 1],
    [6,  21, 25, 0, 0.1, 1],
    [7,  35, 40, 1, 0.5, 0],
    [8,  48, 45, 2, 0.35, 0],
    [9,  35, 40, 2, 0.4, 1],
    [10, 37, 54, 2, 0.45, 0],
    [11, 18, 25, 0, 5.0, 1],
    [12, 24, 40, 1, 0.4, 1],
    [13, 33, 45, 2, 3.0, 0],
    [14, 45, 50, 1, 4.0, 1],
]
val = [
    [15,  38, 50, 2, 2.5, 0],
    [16,  24, 25, 1, 5.0, 1],
    [17,  42, 30, 3, 4.0, 0],
    [18,  36, 47, 2, 3.0, 0],
    [19,  23, 35, 0, 1.5, 1],
    [20,  40, 45, 2, 4.5, 0],
]

test = [
    [21,  35, 30, 2, 5.0, 1],
]

analyze(train)
analyze(val)
analyze(test)