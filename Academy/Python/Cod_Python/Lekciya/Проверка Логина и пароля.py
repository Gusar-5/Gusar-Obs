l = 123
p = 234

l1 = int(input("Введите логин: "))

if l1 == l:
    print("\tЛогин верный")
    
    for i in range(3):
        p1 = int(input(f"Введите пароль (3 попытки): {i + 1} попытка: "))

        if i == 2:
            print(f"Пароль не верный. "\
                  "Доступ не разрешен\n"), exit()  
        elif p1 != p:
            print(f"\tПароль не верный")               
        else:
            print("Пароль верный")
            print("\tДоступ разрешен"), exit()

else:
    print("Логин не верный! Попробуйте снова")
