print('\nУсловия покупки конфет:\n==Если вес больше 2 кг то цена 200р/кг, если менее то 250р/кг==')
while True:
    mass = float(input('\nВведите желаемое количество конфет (в граммах): '))
    mass /= 1000
    if mass <= 0:
        print('\nВы ввели некорректное значение. Попробуйте снова.')
    else:
        money = 200 if mass >= 2 else 250
        money1 = money * mass
        print(f'\nМасса ваших конфет: {mass:.2f} кг', end =" ")
        print(f'и цена {money} р/кг, равна: {money1:.2f} руб.')
        break
