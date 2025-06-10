g = int(input("Введите горизонталь:\t "))
v = int(input("Введите вертикаль:\t "))
k = "*"
if g > 0 and v > 0:
    for i in range(v):
        print((k + " ") * g)
else:
    print("Вывод искл. положительных чисел. Попробуйте снова:\t ")
