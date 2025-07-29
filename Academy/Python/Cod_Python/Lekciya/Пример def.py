def sum(v, m, g):
    return v + m + g

def cha(z, x, u):
    return (z+1, x-1, u-1)

a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
c = int(input('Введите 3 число: '))

print(sum(a, b, c))
s = sum(a, b, c)
print(s)

print(cha(a, b, c))
s = cha(a, b, c)
print(s)

a, b, c = cha(a, b, c) # Перезаписываем a, b, c
print(a, b, c)

r = int(input('Введите 4 число: '))
t = int(input('Введите 5 число: '))
y = int(input('Введите 6 число: '))
print(f'Сумма чисел: {sum(a, b, c)}')
p = sum(r, t, y)
print('Сумма чисел: ', p)

r, t, y = cha(r, t, y)
m = cha(r, t, y)  # m - теперь строка
print(m)

