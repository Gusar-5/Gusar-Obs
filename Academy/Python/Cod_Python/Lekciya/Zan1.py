def zas(x):
    while True:
        try:
            x = float(x)
            break
        except ValueError: # Проверка на ошибку типа ввода переменных
            print('Ошибка')
            x = input('Введите целое число еще раз: ')
    return x
 
# a = input('Введите число: ')
# b = 0
# for i in a:
#     b += zas(i)
#     print(i)
# print(f'Сумма {b:.0f}')

a = input('Введите число: ')
c = len(a)
a = zas(a)
b = 0
for i in range(c, i - 1, -1):
    r = a % 10
    a = a // 10
    b += r
    print(r)
print(b)