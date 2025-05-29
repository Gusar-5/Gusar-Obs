# Вывести числа 0 до n, где n - это случайное число из списка
import random
n = [3, 7, 10, 15]
bot = random.choice(n)
print(f"\nРандом от 0 до", bot)
for i in range(0, bot + 1):
    print(i, end=' ') 