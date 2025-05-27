# Вывести максимальное число из введенных четырех
n = []
# Ввод четырех чисел
for _ in range(4):
    number = int(input("Введите число: "))
    n.append(number)
# Находим максимальное число
maximum = n[0]
for i in n:
    if i > maximum:
        maximum = i
print("Максимальное число:", maximum)  # Вывод: максимальное число