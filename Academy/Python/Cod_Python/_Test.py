while True:
    s = int(input("Введите начальное число: "))
    e = int(input("Введите конечное число: "))

    if s == e:
        print("Значения равные, попробуйте снова.")
        continue

    # Определяем направление и стартовые значения для цикла
    if s < e:
        start = e if e % 2 == 0 else e - 1
        end = s
    else:
        start = s if s % 2 == 0 else s - 1
        end = e

    # Выводим числа с шагом -2 от start до end (не включая end)
    for i in range(start, end - 1, -2):
        print(i, end=" ")
    print()
    break
    