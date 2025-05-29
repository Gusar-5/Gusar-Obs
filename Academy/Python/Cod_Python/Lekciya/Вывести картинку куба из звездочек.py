# Вывести картинку куба из звездочек

v = int(input("Введите число: "))
a = ""; b = "*"
for i in range(v):
    print(a)
    for i in range(v):
        print(b, end = " ") # С пробелом красивей

# Оказывается так можно было c 1 for
print("\nОказывается так можно было: ")
v = int(input("Введите число: "))
a = "*"
for i in range(v):
    print(a * v)

# А так красивей
print("\nА так красивей: ")
v = int(input("Введите число: "))
a = "*"
for i in range(v):
    print((a + " ") * v)
