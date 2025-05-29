# Вывести нечентые числа с убыванием, A > B
A = int(input("Введите 1 число: "))
B = int(input("Введите 2 число: "))

for i in range(A - (A + 1) % 2, B - 1, - 2):
    print(i, end=' ') 