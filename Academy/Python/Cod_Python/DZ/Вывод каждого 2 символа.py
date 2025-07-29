# Вывод искомого слова
a = input('\nВведите строку: ')
b = len(a)
for i in range(1, b, 2):
    print(a[i], end = ' ')
print('\n')