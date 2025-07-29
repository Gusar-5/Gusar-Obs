# Все функции ошибок BaseException
 
a = 3
b = 5

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
else: # Будет если try верно, в except не зайдет
    print('else тут это Продолжение try')
finally:
    print(a / b) # Выполнится влюбом случае независимо Сработал ли try или вышла Ошибка
# Либо используем else вместо finally
