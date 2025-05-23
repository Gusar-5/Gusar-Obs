while True:
    print("Сравнение чисел")
    f = float(input("\nВведите 1 целое число: "))
    s = float(input("Введите 2 целое число: "))    
    if f == s:
        print("\nЗначения равные. Попробуйте снова.")
    else:
        g =  f if f > s else s
        print(f"\nЗначения {g} наибольшее")
        print()
