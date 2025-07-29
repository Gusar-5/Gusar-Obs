# Расчет объема куба
while True:
    try:
        z = input("\nВведите длину куба: ")
        v = int(z)
        if v <= 0:
            print(f'Вы ввели {v}. Введите положительное число')
            continue        
        V = v ** 3
        print (f'Объем куба c длиной {v} равен: {V}\n')
        break
    except ValueError:
        print(f'Ошибка ввода. Вы ввели {z}. Введите число') 