# Срезы
a = input('Введите строку: ')
b = input('Введите слово, которое хотите найти: ')
print(b in a)
if b in a:
    print('Слово найдено')
else:
    print('Слово не найдено')


print(a[::-1])
print('мир' in a) # Вывод True или False

s = ['Анна', 'Мария', 'Миша', 'Коля']
print(s)
t = s[1:] # с 1 и до конца
print(t)

t = s[::2] # Каждое второе
print(t)
print()

for i in range(len(s)): # или for i in s:
    print(s[i] [1:], end = ' ') # или print(i[1:], end = ' ')