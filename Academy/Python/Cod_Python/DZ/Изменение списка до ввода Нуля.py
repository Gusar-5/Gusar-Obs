# Изменение списка до ввода Нуля
spisok = [1, 2, 3, 4, 5]
print('\nСписок чисел:', spisok)

def viv(main):
     spisok[main] = int(input('Введите число для замены: '))
     print('\nОбновленный список:', spisok)

i = 0
while True:
    main = int(input('Введите какое число в списке хотите поменять,'
                     ' (или введите 0 для выхода): '))                  
                   
    if main not in (0, 1, 2, 3, 4, 5):
        print ('\nНеправильный ввод')
        continue    
    elif main == 0:
        print ('\nДо свиданья.\n')
        break
    else:
        viv(main - 1)
        continue        
                    