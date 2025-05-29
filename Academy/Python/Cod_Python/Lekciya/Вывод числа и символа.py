# Вывод числа и символа
a = int(input("Вывод числа: "))
b = input("Вывод символа: ")
c = len(str(b))
if a > 0 and c == 1:
    for i in range(a):
        print(b, end = " ")
else:
    print("Не коректный ввод ")