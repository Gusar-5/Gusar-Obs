# ASCII Вывод кода строки
'''
1 вариант

'''
a = input('\nВведите строку из букв: ')

if a.isalpha():
    for i in range(len(a)):
        b = ord(a[i])  # получаем ASCII-код символа
        print(b, end = ' ')            
else:
    print ('Не верно. Ввод со знаками и цифрами\n')
'''
2 вариант

'''
def kod(c):
    return ord(c) # Возвращаем ASCII-код символа

a = input('\nВведите строку из букв: ')

if a.isalpha():
    for i in a:
        print(kod(i), end=' ')
    print()
else:
    print('Не верно. Ввод со знаками и цифрами\n')
