while True:
    try:
        a = int(input('Введите число: '))
        s = 0  # Переменная для хранения суммы цифр
        if a > 0:
            while a > 0:
                b = a % 10
                print(b)
                s += b 
                a //= 10
        else:
            print('Введите положительное число')
        print(s)
        continue
    except ValueError: # Проверка на ошибку типа ввода переменных
        print('Ошибка')
        continue