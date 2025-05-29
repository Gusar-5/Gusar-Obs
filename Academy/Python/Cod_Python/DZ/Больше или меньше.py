print("Сравнение чисел.")
while True:
    f = float(input("\nВведите 1 число: "))
    s = float(input("Введите 2 число: "))    
    if f == s:
        print("\nЗначения равные. Попробуйте снова.")
    elif f > s:
        print(f"\nЗначение {f} больше {s}.")
        break  # Выход из цикла
    else:
        print(f"\nЗначение {s} больше {f}.")
        break  # Выход из цикла
    
 
