import random  
print("Добро пожаловать в игру камень-ножницы-бумага\n")  
for i in range(3):  
    bot = random.choice(["камень", "ножницы", "бумага"])  
    answer = input("Введите камень, ножницы или бумага: ").lower()  
    print(f"Бот выбрал: {bot}")  
    if answer == bot:  
        print("Ничья")  
    elif (answer == "бумага" and bot == "камень") or (answer == "ножницы" and bot == "бумага") or (answer == "камень" and bot == "ножницы"):  
        print("Победа")  
    elif (answer == "камень" and bot == "бумага") or (answer == "бумага" and bot == "ножницы") or (answer == "ножницы" and bot == "камень"):  
        print("Проигрыш")  
    else:  
        print("Некорректный ввод")