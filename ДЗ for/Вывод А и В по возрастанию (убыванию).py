# Вывод А и В по возрастанию (убыванию)

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

if A < B:
    B += 1
    for i in range(A, B): # по возрастанию
        print(i, end=" ")
elif A > B:
    A += 1  
    for i in range(A - 1, B - 1, -1): # по убыванию
        print(i, end=" ")
else:
    print(A, "- числа равные")    
