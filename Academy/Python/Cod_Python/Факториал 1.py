a = int(input("Введите число для вывода Факториала: "))
b = 1
for i in range(1, a + 1):
    b *= i
    print(b)