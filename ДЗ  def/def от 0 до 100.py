# Вывод от 0 до 100
def viv(a):
    return a + 1

a = 0
while a <= 100:
    print(a, end = ' ')
    a = viv(a) 