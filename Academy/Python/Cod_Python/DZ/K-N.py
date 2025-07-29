# Игра: Крестики-Нолики
import random
import time

def proverka(a, b):
    while (a < 0 or a > 2) or (b < 0 or b > 2):
        print('Введено некорректное значение')
        a = int(input('Введите номер строки: '))-1
        b = int(input('Введите номер столбца: '))-1
    return (a, b)

def xod (a, b):
    while pole[a][b] == '0' or pole[a][b] == 'X':
        print('Клетка занята')
        a = int(input('Введите номер строки: '))-1
        b = int(input('Введите номер столбца: '))-1
        a, b = proverka(a, b)
    return (a, b)

def vin(count):
    if pole [0][0] == pole[1][1] == pole[2][2] and pole [0][0] != "-":
        count = 1
    elif pole [0][2] == pole[1][1] == pole[2][0] and pole [1][1] != "-":
        count = 1
    else:
        for i in range(3):
            if pole [i][0] == pole[i][1] == pole[i][2] and pole [i][0] != "-":
                count = 1
                break
            elif pole [0][i] == pole[1][i] == pole[2][i] and pole [0][i] != "-":
                count = 1
                break
    return (count)

kubik = [1, 2, 3, 4, 5, 6]
def brosok(u1, u2): # Определение очередности хода - бросок кубика
        while True:            
            u1 = input(f'\nКубик бросает {u1} игрок\n'
                    'Нажмите любую конопку для броска:')            
            u1 = random.choice(kubik)            
            print('Бросок:', end=' ', flush=True)
            for _ in range(3):
                print('.', end='', flush=True)
                time.sleep(1)
            print(f' {u1}')
            u2 = input(f'\nКубик бросает {u2} игрок\n'
                    'Нажмите любую конопку для броска:')            
            u2 = random.choice(kubik)
            print('Бросок:', end=' ', flush=True)
            for _ in range(3):
                print('.', end='', flush=True)
                time.sleep(1)
            print(f' {u2}')
            if u1 == u2:
                print('\nЗначения равные. Бросам кубик повторно')
                continue 
            return (u1, u2)

print('\n Игра: Крестики-Нолики')
pole = [["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]]
for i in pole:
    print(i)

while True:
    menu = int(input('\nВыберите режим игры:\n'
                     '1 - 2 игрока (игрок против игрока)\n'
                     '2 - Игрок и компьтер (Бот)\n'))    
    if menu not in [1, 2]:
        print(f'Ошибка выбора режима')
        continue   
       
    if menu == 1: # игрок против игрока
        print('\nРежим - "Игрок против игрока"')
        time.sleep(1.5) 
        print('\nКидаем кубик для определения кто будет ходить первым')
        time.sleep(1.5)
        u1, u2 = brosok('первый', 'второй') # Бросок кубика (Отправляем "строку", а получаем цифровое значение)

        m = max(u1, u2) # Чей бросок больше
        if m == u1: # Кто первый ходит (надо тоже через def сделать)
            print(f'\n"{u1}" у 1 игрока и, "{u2}" у 2 игрока, 1 игрок ходит первым')
            time.sleep(3)        
        else:
            print(f'\n"{u1}" у 1 игрока и, "{u2}" у 2 игрока, 2 игрок ходит первым')
            time.sleep(3)        

        while True: # Победитель выбирает чем будет играть 0 или Х
            f = input(f'\nВведите чем будите играть "0" или "Х": ')
            if f not in ["0", "X"]:
                print(f'Ошибка выбора режима')
                continue
            elif f in ["0", "X"] and f == "0":
                u1 = f; u2 = "X"
            elif f in ["0", "X"] and f == "X":
                u1 = f; u2 = "0"
            
            f1 = u1 # Переменная для смены игрока для хода
            count = 0 # Переменная определения победителя
            hag = 0 # Переменная для подсчета колличества ходов

            while count == 0 and hag != 9:            
                print(f'\nХод игрока {f1}')
                a = int(input('Введите номер строки: '))-1
                b = int(input('Введите номер столбца: '))-1
                a, b = proverka(a, b)
                a, b = xod(a, b)
                pole[a][b] = f1
                print('Ход сделан')
                hag += 1
                
                for i in pole:
                    print(i)
                
                # Меняем игрока после каждого хода
                if f1 == u1:
                    f1 = u2
                else:
                    f1 = u1

                count = vin(count) # Определяем победителя
                if count == 1:
                    print(f'\nПобеда игрока {f1}')
                    break

            if hag == 9: # Определяем колличество ходов (будет ли Ничья)
                print('\nНичья')
                break        
        
    if menu == 2: # игрок против Компьютера
        print('\nРежим - "Игрок против Компьютера"')
        time.sleep(1.5) 
        print('\nКидаем кубик для определения кто будет ходить первым')            
        time.sleep(1.5)
        u1, u2 = brosok('Игрок', 'Компьютер') # Бросок кубика (Отправляем "строку", а получаем цифровое значение)

        m = max(u1, u2) # Чей бросок больше
        if m == u1: # Кто первый ходит
            print(f'\n"{u1}" у Игрока и, "{u2}" у Компьютера, Игрок ходит первым')
            time.sleep(3)
        else:
            print(f'\n"{u1}" у Игрока и, "{u2}" у Компьютера, Компьютер ходит первым')
            time.sleep(3)
     