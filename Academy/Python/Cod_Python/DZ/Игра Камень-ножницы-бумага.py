import random
print("Игра: Камень-ножницы-бумага")
for i in range(3):
    bot = random.choice(["Камень", "Ножницы", "Бумага"])
    wod = input("Введите любое слово: Камень, Ножницы, Бумага \n").lower
    print(bot)
    if wod != bot:
        print("Не корректный ввод попробуйте снова")
        if wod == bot:
            print("Ничья")     
        elif wod == "камень" and bot == "ножницы":
            print("Вы выиграли")
        elif wod == "ножницы" and bot == "бумага":
            print("Вы выиграли")
        elif wod == "бумага" and bot == "камень":
            print("Вы выиграли")
        else:
            print("Вы проиграли")


