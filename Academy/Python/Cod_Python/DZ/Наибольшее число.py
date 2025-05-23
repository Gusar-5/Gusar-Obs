print("Сравнение чисел")
while True:
    f = int(input("\nВведите 1 целое число: "))
    s = int(input("Введите 2 целое число: "))    
    if f == s:
        print("\nЗначения равные. Попробуйте снова.")
    elif f > s:
          f = g
    else:
        g = s
        print(f"\nЗначения {g:.0f} наибольшее")
        print()
        break  # Выход из цикла