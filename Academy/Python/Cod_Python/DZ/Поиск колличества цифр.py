# Поиск колличества цифр
a = input('\nВведите строку: ')
print ()
for i in range(10):      
    if a.count(f'{i}'):
        print (f'Колличество {i}:', a.count(f'{i}')) 
print ()