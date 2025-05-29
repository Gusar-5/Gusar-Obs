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



