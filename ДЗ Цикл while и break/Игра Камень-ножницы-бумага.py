import random
print("Игра: Камень-ножницы-бумага")
print("Начинаем игру...До 3-х побед!")
bot_i = 0
user_i = 0

while user_i < 3 and bot_i < 3: # Игра до 3х побед    
    
    bot = random.choice(["камень", "ножницы", "бумага", "ящерица", "спок"])
    user = input("Выберите: Камень\n"
                "\t  Ножницы     \n"
                "\t  Бумага      \n"
                "\t  Ящерица     \n"
                "\t  Спок        \n").lower()
    
    if user not in ["камень", "ножницы", "бумага", "ящерица", "спок"]:
        print(f"Вы ввели некорректные данные {user}, попробуйте снова")
        continue
    print(f"Вы заявили: {user}. Бот выбрал: {bot}.")
    if user == bot:
        print("Ничья\n")
    elif(user == "ножницы"  and bot == "бумага" )  or \
        (user == "бумага"   and bot == "камень" )  or \
        (user == "камень"   and bot == "ящерица")  or \
        (user == "ящерица"  and bot == "спок"   )  or \
        (user == "спок"     and bot == "ножницы")  or \
        (user == "ножницы"  and bot == "ящерица")  or \
        (user == "ящерица"  and bot == "бумага" )  or \
        (user == "бумага"   and bot == "спок"   )  or \
        (user == "спок"     and bot == "камень" )  or \
        (user == "камень"   and bot == "ножницы"):
        user_i += 1 # Счет игрока
        print(f"Ваша победа: {user_i} : {bot_i}\n")
    else:
        bot_i += 1 # Счет бота
        print(f"Бот победил: {user_i} : {bot_i}\n")
# За кем победа
if user_i == 3:
        print(f"Вы победили над Ботом! \n")        
elif bot_i == 3:
    print(f"В этой игре победа за Ботом \n")
