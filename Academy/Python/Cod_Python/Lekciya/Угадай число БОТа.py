# Угадай число БОТа

import random
bot = random.randint(1, 100)

user = int(input("Угадай число БОТа: "))
while user != bot:
    print("Не угадали: ")
    if user < bot:
        print("Ваше число меньше, чем у БОТа!")
    else:
        print("Ваше число больше, чем у БОТа!")
    user = int(input("Угадай число БОТа: "))
print("Вы угадали!\n")