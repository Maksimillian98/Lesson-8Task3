m = int(input("Введите максимальную массу одной лодки в КГ: "))
n = int(input("Введите количество рыбаков: "))

if m <= 0 or m > 10**6:
    print("Ошибка: неверная грузоподъёмность")
elif n <= 0 or n > 100:
    print("Ошибка: неверное количество рыбаков")
else:
    weights = []
    for _ in range(n):
        weight = int(input("Введите вес рыбака: "))
        if 1 <= weight <= m:
            weights.append(weight)
        else:
            print("Ошибка: вес рыбака некорректен")
    weights.sort()

    boat_count = 0
    i, j = 0, len(weights) - 1

    while i <= j:
        if weights[i] + weights[j] <= m:
            i += 1
        j -= 1
        boat_count += 1

    print(boat_count)
