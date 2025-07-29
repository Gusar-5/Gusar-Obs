# Вывод строки по параметрам
line_input = input('\nВведите строку: ')

# Ввод начального значения
while True:
    try:
        start = int(input('Введите начальное число (от 0 до длины строки): '))
        if start < 0:
            print('Введенное значение должно быть положительным или равно нулю.')
            continue
        if start > len(line_input):
            print(f'Начальное значение не может быть больше длины строки ({len(line_input)}).')
            continue
        break
    except ValueError:
        print('Некорректный ввод. Попробуйте снова.')

# Ввод конечного значения
while True:
    try:
        stop = int(input('Введите конечное число (больше начального): '))
        if stop <= start:
            print(f'Конечное значение должно быть больше начального ({start}).')
            continue
        if stop > len(line_input):
            print(f'Длина строки: {len(line_input)} символ(а,ов). Введите значение равное длине или меньшее.')
            continue
        break
    except ValueError:
        print('Некорректный ввод. Попробуйте снова.')

# Ввод шага
while True:
    try:
        step = int(input('Введите шаг (не равен нулю): '))
        if step == 0:
            print('Шаг не может быть равен нулю.')
            continue
        elif step < 0:
            print('Введенное значение должно быть положительным или равно нулю.')
            continue
        break
    except ValueError:
        print('Некорректный ввод. Попробуйте снова.')

# Вывод результата
print()
print(f'Выводим строку с начальным индексом {start}, конечным индексом {stop}, и шагом {step}')
print(f'Начальная строка: {line_input}')
print(f'Результат: {line_input[start:stop:step]}') 
print()      
