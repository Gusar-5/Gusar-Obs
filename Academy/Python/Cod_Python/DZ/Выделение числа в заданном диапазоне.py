# Выделение числа в заданном диапазоне
while True:
    print("\nВыделение числа !x! в заданном диапазоне")
    a = int(input("Введите начало диапазона:\t      "))
    b = int(input("Введите конец диапазона:\t      "))
    while True:
        if a == b:
            print(f"Диапазоны равные. Попробуйте снова.")
            break
        elif a > b:
            a, b = b, a # Если пользователь ввел начальный диапазон больше конечного            
        c = int(input(f"Введите число в диапазоне от {a} до {b}: "))            
        if a < b and c >= a and c <= b:            
            for i in range(a, b + 1):
                if i == c:
                    print(f"!{i}!", end=" ")
                else:
                    print(i, end=" ")
            exit("\n")        
        else:
            c < a or c > b
            print(f"Число {c} не входит в указанный диапазон\n")                    
        continue
    