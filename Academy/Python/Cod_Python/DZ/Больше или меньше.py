print("Сравнение чисел.")
while True:
    f = float(input("\nВведите 1 число: "))
    s = float(input("Введите 2 число: "))    
    if f == s:
        print("\nЗначения равные. Попробуйте снова.")
    elif f > s:
        print(f"\nЗначения {f} больше {s}.")
        break  # Выход из цикла
    else:
        print(f"\nЗначения {s} больше {f}.")
        break  # Выход из цикла
    