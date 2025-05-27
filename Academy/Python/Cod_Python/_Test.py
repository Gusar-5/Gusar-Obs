# Вывести нечентые числа с убыванием, A > B
A = int(input("Ввод 1 числа: "))
B = int(input("Ввод 2 числа: "))

for i in range(A - (A + 1) % 2, B - 1, - 2):
    print(i, end=' ') 
