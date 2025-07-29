# Калькулятор М
'''
      1 Вариант
Получился Объемистым
'''
while True:    
    menu = input('\nВыберите:\n' \
    '1 - Сложение\n' \
    '2 - Вычетание\n' \
    '3 - Умножение\n' \
    '4 - Деление\n' \
    '0 - Выход\n')        
    try:
        menu = int(menu)    
    
        if menu < 0 or menu > 4:
            print('Ошибка выбора. Введите: 1, 2, 3, 4 или 0 для выхода')
        elif menu == 1: # Сложение
            print('\n"Сложение"')
            while True:
                try:
                    s1 = int(input('Введите первое слагаемое: '))
                    while True:
                        try:
                            s2 = int(input('Введите второе слагаемое: '))
                            s = s1 + s2
                            print(f'\nСумма слагаемых "{s1}" + "{s2}" равна: {s}')
                            break                            
                        except ValueError:
                            print('Ошибка ввода второго слагаемого. Попробуйте еще раз.')
                    break
                except ValueError:
                    print('Ошибка ввода первого слагаемого. Попробуйте еще раз.') 

        elif menu == 2: # Вычитание 
            print ('\n"Вычитание"')
            while True:
                try:
                    s1 = int(input('Введите уменьшаемое: '))
                    while True:
                        try:
                            s2 = int(input('Введите вычитаемое: '))
                            s = s1 - s2
                            print(f'\nРазность "{s1}" - "{s2}" равна: {s}')
                            break
                        except ValueError:
                            print('Ошибка ввода вычитаемое. Попробуйте еще раз.')
                    break
                except ValueError:
                    print('Ошибка ввода уменьшаемого. Попробуйте еще раз.') 

        elif menu == 3: # Умножение
            print('\n"Умножение"')
            while True:
                try:
                    s1 = int(input('Введите 1 множитель: '))
                    while True:
                        try:
                            s2 = int(input('Введите 2 множитель: '))
                            s = s1 * s2
                            print(f'\nПроизведение множителей "{s1}" * "{s2}" равна: {s}')
                            break
                        except ValueError:
                            print('Ошибка ввода 2 множителя. Попробуйте еще раз.')
                    break
                except ValueError:
                    print('Ошибка ввода 1 множителя. Попробуйте еще раз.')

        elif menu == 4: # Деление
            print('\n"Деление"')
            while True:
                try:
                    s1 = int(input('Введите делимое: '))
                    while True:
                        try:
                            s2 = int(input('Введите делитель: '))        
                            try:
                                print(f'\nЧастое "{s1}" / "{s2}" равно: {s1 / s2}')
                                break
                            except ZeroDivisionError:
                                print('\n"На ноль делить нельзя!"\n')
                        except ValueError:
                            print('Ошибка ввода делителя. Попробуйте еще раз.')
                    break
                except ValueError:
                    print('Ошибка ввода делимого. Попробуйте еще раз.')
                    
        elif menu == 0:
            print('\nДо свиданья\n')
            break      

    except ValueError:                    
        print(f'Вы выбрали "{menu}".\n'
              'Выберите: 1, 2, 3, 4 или 0 для выхода')
        
    while True:
        return_menu = input('\nЖелете новый выбор? (Да/Нет): ').strip().lower()
        if return_menu not in ('да', 'нет'):
            print('Некорректный ввод.')
            continue
        elif return_menu == 'да':
            break
        elif return_menu == 'нет':
            print('До свиданья.\n')
            exit()
'''
       2 Вариант
Оказывается так можно было!
в "def" вставить проверку
КОД стал приятнее выглядеть
'''
# def proverka(nomer):
#     while True:
#         try:
#             return int(input(nomer))
#         except ValueError:
#             print('Ошибка ввода. Пожалуйста, введите числовое значение.')

# while True:    
#     menu = proverka('\nВыберите:\n' \
#     '1 - Сложение\n' \
#     '2 - Вычетание\n' \
#     '3 - Умножение\n' \
#     '4 - Деление\n' \
#     '0 - Выход\n')        
    
#     if menu == 0:
#         print('\nДо свиданья\n')
#         break
#     elif menu < 0 or menu > 4:
#         print('Ошибка выбора. Введите: 1, 2, 3, 4 или 0 для выхода')
#         continue
#     elif menu == 1: # Сложение
#         print('\n"Сложение"')
#         s1 = proverka('Введите первое слагаемое: ')
#         s2 = proverka('Введите второе слагаемое: ')
#         s = s1 + s2
#         print(f'\nСумма слагаемых "{s1}" + "{s2}" равна: {s}')                     

#     elif menu == 2: # Вычитание 
#         print ('\n"Вычитание"')            
#         s1 = proverka('Введите уменьшаемое: ')           
#         s2 = proverka('Введите вычитаемое: ')
#         s = s1 - s2
#         print(f'\nРазность "{s1}" - "{s2}" равна: {s}')                            

#     elif menu == 3: # Умножение
#         print('\n"Умножение"')
#         s1 = proverka('Введите 1 множитель: ')
#         s2 = proverka('Введите 2 множитель: ')
#         s = s1 * s2
#         print(f'\nПроизведение множителей "{s1}" * "{s2}" равна: {s}')                            

#     elif menu == 4: # Деление
#         print('\n"Деление"')
#         s1 = proverka('Введите делимое: ')
#         while True:
#             s2 = proverka('Введите делитель: ')
#             try:
#                 print(f'\nЧастое "{s1}" / "{s2}" равно: {s1 / s2}')
#                 break
#             except ZeroDivisionError:
#                 print('\n"На ноль делить нельзя!"\n') 

#     while True:
#         return_menu = input('\nЖелете новый выбор? (Да/Нет): ').strip().lower()
#         if return_menu not in ('да', 'нет'):
#             print('Некорректный ввод.')
#             continue
#         elif return_menu == 'да':
#             break
#         elif return_menu == 'нет':
#             print('До свиданья.\n')
#             exit()
'''
       3 Вариант
Добавил 2 "def" сократил не много,
но получилось интерестно
'''
# def proverka(nomer):
#     while True:
#         try:
#             return int(input(nomer))
#         except ValueError:
#             print('Ошибка ввода. Пожалуйста, введите числовое значение.')

# def chastnie(n1, n2):
#     s1 = proverka(n1)
#     s2 = proverka(n2)
#     return s1, s2

# while True:    
#     menu = proverka('\nВыберите:\n' \
#     '1 - Сложение\n' \
#     '2 - Вычетание\n' \
#     '3 - Умножение\n' \
#     '4 - Деление\n' \
#     '0 - Выход\n')        
    
#     if menu == 0:
#         print('\nДо свиданья\n')
#         break
#     elif menu < 0 or menu > 4:
#         print('Ошибка выбора. Введите: 1, 2, 3, 4 или 0 для выхода')
#         continue
#     elif menu == 1: # Сложение
#         print('\n"Сложение"')
#         s1, s2 = chastnie('Введите первое слагаемое: ', 'Введите второе слагаемое: ')        
#         s = s1 + s2
#         print(f'\nСумма слагаемых "{s1}" + "{s2}" равна: {s}')                     

#     elif menu == 2: # Вычитание 
#         print ('\n"Вычитание"')
#         s1, s2 = chastnie('Введите уменьшаемое: ', 'Введите вычитаемое: ')
#         s = s1 - s2
#         print(f'\nРазность "{s1}" - "{s2}" равна: {s}')                            

#     elif menu == 3: # Умножение
#         print('\n"Умножение"')
#         s1, s2 = chastnie('Введите первый множитель: ', 'Введите второй множитель: ')
#         s = s1 * s2
#         print(f'\nПроизведение множителей "{s1}" * "{s2}" равна: {s}')                            

#     elif menu == 4: # Деление
#         print('\n"Деление"')
#         s1 = proverka('Введите делимое: ')
#         while True:
#             s2 = proverka('Введите делитель: ')
#             try:
#                 print(f'\nЧастое "{s1}" / "{s2}" равно: {s1 / s2}')
#                 break
#             except ZeroDivisionError:
#                 print('\n"На ноль делить нельзя!"\n') 

#     while True:
#         return_menu = input('\nЖелете новый выбор? (Да/Нет): ').strip().lower()
#         if return_menu not in ('да', 'нет'):
#             print('Некорректный ввод.')
#             continue
#         elif return_menu == 'да':
#             break
#         elif return_menu == 'нет':
#             print('До свиданья.\n')
#             exit()