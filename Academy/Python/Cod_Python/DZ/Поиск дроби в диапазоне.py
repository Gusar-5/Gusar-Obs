# Поиск дроби в диапазоне
def pro(a):
    while True:
        a = float(input('\nВведите дрообное число от 0 до 10:\n'))
        if a < 0 or a > 10:
            print(f'Число {a:.0f} вне диапазона')
            continue
        if a % 1 == 0:
            print(f'Число {a:.0f} целое. Введите дробное.')
            continue
        else:
            print(f'Введено дробное число: {a}\n'
                   'До свиданья\n')
        return (a)
a = float()
pro(a)