
[[Язык программирования Python]]

# [[Общие сведения]]

# Переменные

-  называются буквами и символами, (**w** или **dikdt5**), всегда начало с букв
- **int**  - целое число
- **float** - все дробные числа
- **string** - строки и символы
- **bool** - логическая переменная у нее 2 значения (**True** или **False**)
- **\n**  - перенос на другую сточку "Площадь равна\n", a....
- сокращение кода:
**a = 5**
**a = a + 5** или **a += 5**
![[Pasted image 20250506205210.png]]

- **INPUT** () - ввод значений.  и прием их как строчное значение - **string**
**int(input())** - ввод целого числа
![[Pasted image 20250506205108.png]]

![[Pasted image 20250506211432.png]]
a = int(input("Введите сколько было котлет"))
a += int(input("Отлично! Введите теперь сколько котлет он нашел"))
a -= int(input("Отлично! А теперь введите сколько кот съел котлет"))
print("У кота осталось", a, "котлет")

Двойной **Tab** 
![[Pasted image 20250508193117.png]]

**sep="*", end="."**
![[Pasted image 20250508193449.png]]

**Замена кавычек на переменную f:**
![[Pasted image 20250508194534.png]]

Возведение в степень двумя звездочками **
r = e ** u
Округление в меньшую сторону двумя слешами (Целочисленное деление) //
r = e // u
Остаток от деления процентом %
r = e % u

a = int(input("Введите четырехзначное число для зеркального отображения ")) ==1234==
b = a % 10 # = ==4==
a = a // 10 #  = 123
c = a % 10 # = ==3==
a = a // 10 #  = 12
i = a % 10 # = ==2==
a = a // 10 #  = 12
w = a % 10 # = 3
print(b,c,i,w, sep = "")
print(f"{b}{c}{i}{w}")
![[Pasted image 20250508212051.png]]

==Сок стоит 14р 50к. Сколько коробок сока можно купить на 80 р? Сколько нужно добавить, чтобы купить еще 1 коробку?==

sok = 14.5 # Цена за коробку сока
many = 80 # у нас денег
itog = many // sok # Сколько сока можем купить на 80 руб
many1 = many - itog * sok  # Сколько денег останется.
many2 = sok - many1 # Сколько денег нужно добавить для покупки еще 1 коробки сока.
print(f"У нас есть {many} руб., а сок стоит {sok} руб/за штуку")
print (f"\nВ итоге на {many} руб мы можем купить {itog} коробок сока ")
print (f"У нас останется {many1} руб")
print (f"Нам нужно добавить еще {many2} руб, чтоб купить еще 1 коробку сока")

![[Pasted image 20250512151936.png]]

many = float(input("Введите сколько денег у нас есть для покупки сока?: "))
sok = float(input("Введите сколько стоит сок?: "))
maks = int(input("Введите сколько коробок сока нужно купить?: "))
if many >= sok:
    itog = many // sok
    many1 = many - itog * sok
    many2 = maks * sok
    many3 = maks * sok - many
    print (f"\nВ итоге на {many:.2f} руб мы можем купить {itog} коробок сока ")
    print (f"У нас останется {many1:.2f} руб")
    print (f"Чтобы купить {maks} коробки сока, по {sok:.2f} за штуку,", end=" ")
    print (f"нам нужно {many2:.2f} руб., нам не хватает {many3:.2f} руб")
else:
    print(f"\nУ нас недостаточно денег для покупки сока.")
    many2 = maks * sok
    many3 = maks * sok - many
    print (f"\nЧтобы купить {maks} коробки сока, по {sok:.2f} за штуку,", end=" ")
    print (f"нам нужно {many2:.2f} руб., нам не хватает {many3:.2f} руб")

![[Pasted image 20250512170422.png]]

many = float(input("Введите сколько денег у нас есть для покупки сока?: "))
sok = float(input("Введите сколько стоит сок?: "))
maks = int(input("Введите сколько коробок сока нужно купить?: "))
many2 = maks * sok
many3 = many2 - many
if many >= sok:
    itog = many // sok
    many1 = many - itog * sok
    print(f"\nВ итоге на {many:.2f} руб мы можем купить", int(itog), "коробок сока ")
    print(f"У нас останется {many1:.2f} руб")
else:
    print(f"\nУ нас недостаточно денег для покупки сока.")
print(f"\nЧтобы купить {maks} коробки сока, по {sok:.2f} за штуку,", end=" ")
print(f"нам нужно {many2:.2f} руб., нам не хватает {many3:.2f} руб")

![[Pasted image 20250512171136.png]]


