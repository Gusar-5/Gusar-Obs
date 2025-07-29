try:
    a = int(input('\nВведите 1 число: '))
    b = int(input('Введите 2 число: '))        
    print(a // b)    
except ZeroDivisionError:
    print('На Ноль делить нельзя')
except ValueError:
    print('Введите числа')
except Exception:
    print('Любая ошибка')  