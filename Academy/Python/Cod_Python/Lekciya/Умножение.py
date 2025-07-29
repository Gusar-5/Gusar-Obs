def count():
    a = int(input("Введите 1 число: "))
    b = int(input("Введите 2 число: "))
    return (a, b)

while True:
    main = int(input("Калькулятор:\n"
                    "Для сложения нажмите\t - 1\n"
                    "Для вычитания нажмите\t - 2\n"
                    "Для умножения нажмите\t - 3\n"
                    "Для деления нажмите\t - 4\n"
                    "Для выхода нажмите\t - 0\n"))

    if main not in [0, 1, 2, 3, 4]:
        print ("Неправильный ввод")
        continue
    elif main == 1:
        a, b = count()        
        print({a + b})
        continue
    elif main == 2:
        a, b = count()        
        print({a - b})
        continue        
    elif main == 3:
        a, b = count()        
        print({a * b})
        continue
    elif main == 4:
        a, b = count()        
        if b != 0:
            print(f"Результат деления: {a / b}")
        else:
            print("Ошибка: деление на ноль") 
        continue
    elif main == 0:  
        print("Выход\n")     
        break

# Другой калькулятор
# def count():
#     a = int(input("Введите 1 число: "))
#     b = int(input("Введите 2 число: "))
#     return (a, b)

# def s(a, b, m): 
#     if m == 1:        
#         print(a + b)      
#     elif m == 2:             
#         print(a - b)               
#     elif m == 3:                
#         print(a * b)       
#     elif m == 4:               
#         if b != 0:
#             print(f"Результат деления: {a / b}")
#         else:
#             print("Ошибка: деление на ноль") 

# while True:
#     main = int(input("Калькулятор:\n"
#                     "Для сложения нажмите\t - 1\n"
#                     "Для вычитания нажмите\t - 2\n"
#                     "Для умножения нажмите\t - 3\n"
#                     "Для деления нажмите\t - 4\n"
#                     "Для выхода нажмите\t - 0\n"))

#     if main not in [0, 1, 2, 3, 4]:
#         print ("Неправильный ввод")
#         continue   
#     if main == 0:  
#         print("Выход\n")        
#         break

#     a, b = count()
#     s(a, b, main)