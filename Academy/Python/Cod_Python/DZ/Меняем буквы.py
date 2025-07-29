# Меняем буквы
a = input('\nВведите строку: ').lower()
b = input('Введите символ: ')

if b not in a:
    print("Символ не найден.")
else:
    c = ''
    for i in a:
        if i == b:
            c += i.upper()
        else:
            c += i
    print(f'Результат: {c}')

'''
С "replace" куда проще, хоть и не изучали
'''
print('\n2 вариант:')
a = input('\nВведите строку: ').lower()
b = input('Введите символ: ')

if b in a:
    a = a.replace(b, b.upper()) # Заменяем все вхождения символа b на его заглавную версию
    print(f'{a}\n')
else:
    print("Символ не найден.\n")
    