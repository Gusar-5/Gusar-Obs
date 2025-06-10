# Опрделение НОД, МАХ и MIN чисел
import math

while True: # Меню
    menu = int(input('\nОпрделение НОД, МАХ и MIN чисел\n'
                     '\nВыберите определение: \n'
                     '1 - Наибольший общий делитль\n'
                     '2 - Минимальное число\n'
                     '3 - Максимальное число\n'                    
                     '0 - Выход\n'))                    
                   
    if menu not in [0, 1, 2, 3]: # Проверка ввода
        print ("Неправильный ввод")
        continue
    
    # Поиск НОД
    elif menu == 1:
        print('\nПоиск наибольшего общего делителя:')
        a = int(input('Введите 1 число: '))
        b = int(input('Введите 2 число: '))
        nod = math.gcd(a, b)
        print('Наибольший общий делитель:', nod)
        continue

    # Поиск MIN
    elif menu == 2:
        print('\nОпределение минимального числа:')
        a = int(input('Введите 1 число: '))
        b = int(input('Введите 2 число: '))        
        n = min(a, b)
        if a == b:
            print(f'Введённые числа равны: {a}')
        else:
            print('Минимальное:', n)
            continue

    # Поиск MAX
    elif menu == 3:
        print('\nОпределение максимального числа:')       
        a = int(input('Введите 1 число: '))
        b = int(input('Введите 2 число: '))
        n = max(a, b)
        if a == b:
            print(f'Введённые числа равны: {a}')
        else:
            print('Максимальное:', n)
            continue
    else:
        menu == 0 # Выход
        print('\nДо свиданья\n')
        break