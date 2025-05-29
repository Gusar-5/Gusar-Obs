# Вывести числа от A до B и среднеариффметичесмоке
A = int(input("Вывод 1 числа: "))
B = int(input("Вывод 2 числа: "))
D = 0
t = 0
if A < B:
    for i in range(A, B + 1):
        D += i
        t = t + 1
print(D, D / t)