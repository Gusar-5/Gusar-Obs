# Найти произведение всех нечётных чисел от 1 до 50 включительно.

a = 1
for i in range(1, 51, 2):
    a *= i
print(a)