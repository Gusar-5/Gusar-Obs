# Вывести числа 0 до n, где n - это случайное число из списка
import random
n = [3, 7, 10, 15]
for i in range(1):    
    bot = random.choice(n)
    print(f"\nРандом от 0 до", bot)
    if bot == 3:
        print("0 1 2 3")
    elif bot == 7:
        print("0 1 2 3 4 5 6 7")
    elif bot == 10:
        print("0 1 2 3 4 5 6 7 8")
    else:
        print(" ".join(map(str, range(16))))        
