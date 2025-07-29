# Сумма 10 чисел c "def" и "for"
print('\nСумма 10 чисел')
ob_sum = 0

def summa(a, s):
    return (s + a)

for i in range(10):
    while True:
            try:
                vvod = input(f'Введите {i + 1} число: ')
                vvod = int(vvod)
                break                
            except ValueError:
                print(f'Ошибка ввода. Вы ввели {vvod}. Введите число') 
    ob_sum = summa(vvod, ob_sum)                   

print('Общая сумма:', ob_sum)