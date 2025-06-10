# Изменение списка
spisok = [1, 2, 3, 4, 5]
print('\nСписок чисел:', spisok[0], spisok[1], spisok[2], spisok[3], spisok[4])

while True:
    main = int(input("Введите какое число в списке хотите поменять?: "))                   
                   
    if main not in (1, 2, 3, 4, 5):
        print ("\nНеправильный ввод")
        continue
    elif main == 1:
        spisok[0] = int(input("Введите число для замены: \n"))
        print(spisok[0], spisok[1], spisok[2], spisok[3], spisok[4])
        continue       
    elif main == 2:
        spisok[1] = int(input("Введите число для замены: \n  "))
        print(spisok[0], spisok[1], spisok[2], spisok[3], spisok[4])
        continue
    elif main == 3:
        spisok[2] = int(input("Введите число для замены: \n    "))
        print(spisok[0], spisok[1], spisok[2], spisok[3], spisok[4])
        continue
    elif main == 4:
        spisok[3] = int(input("Введите число для замены: \n      "))
        print(spisok[0], spisok[1], spisok[2], spisok[3], spisok[4])
        continue
    elif main == 5:
        spisok[4] = int(input("Введите число для замены: \n        "))
        print(spisok[0], spisok[1], spisok[2], spisok[3], spisok[4])
        continue
    elif main == 0:
        break