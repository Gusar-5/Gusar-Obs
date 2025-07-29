# Палиндром
import string

a = input("\nВведите строку: ")
# Используем только буквы и цифры
proverka = string.ascii_letters + string.digits
t = ""
for i in a:
    if i in proverka:
        t += i.lower()
if t == t[::-1]:
    print("Введеная строка - палиндром.\n")
else:
    print("Введеная строка - не палиндром.\n")