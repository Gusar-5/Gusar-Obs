# Игра: "Кто первый скажет 100"
import random
print("Игра: Кто первый скажет 100")
print("\tНачинаем игру...")
summa = 0
user = 0
bot = 0
 
while True:        
    user_v = int(input("\nВведите число от 1 до 10: "))  

    if user_v == 0:                    
        print(f"\nВы ввели {user}. Играете в поддавки? Бот умеет игарть! Попробуйте выиграть)")
        continue
    elif user_v >= 100:                    
        print(f"\nЖелаете сразу выиграть? Сразитесь в Ботом по честному. Попробуйте снова")
        continue
    elif user_v < 0:                    
        print(f"\nХотите проиграть? Бот умный! Попробуйте победить)")
        continue
    elif user_v > 10:               
        print(f"\nВы ввели не коректные данные. Попробуйте снова")
        continue
    if 0 < user_v or user_v < 11:
        summa += user_v # Суммируем ввод игрока к общей сумме       
        user = summa # Сумма игрока
        if user >= 100: # Тут Игрок победил
            print(f"\nВаша Сумма {user}, а у Бота {bot}. Вы победили!\n")
            break

    # Бот выбирает число для победы
    if summa >= 90:
        min = 100 - summa
        # Выбираем случайное число
        if min <= 10:
            bot_v = random.randint(min, 10)
        else:
            # теоретически не должно случится, но на всякий случай
            bot_v = random.randint(1, 10)
    else:
        bot_v = random.randint(1, 10)     
    summa += bot_v # Суммируем ввод Бота к общей сумме
    print(f"\t      Бот выбрал: {bot_v}")
    print(f"В сумме: {summa}") # Вывод общей суммы
    bot = summa # Сумма Бота
    if bot >= 100: # Тут Бот победил
        print(f"\nСумма Бота: {bot}, а у Вас: {user}. Бот победил!\n")
        break