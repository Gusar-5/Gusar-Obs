# Вывод Фаренгейт
while True:
    try:
        cel = float(input('\nВведите температуру в Цельсиях: '))
        far = (cel * 9/5) + 32
        print(f'{cel}°C равно {far}°F\n')
    except ValueError:
        print('Введите числовое значение')
        continue

    povtor = input('\nХотите попробовать еще раз? (Да/Нет): ').strip().lower()
    if povtor != 'да':
        break

print('До свиданья.')

# # 2 Вариант (с def)
# def zapros():
#     while True:
#         try:
#             cel = float(input('\nВведите температуру в Цельсиях: '))
#             far = (cel * 9/5) + 32
#             print(f'{cel}°C равно {far}°F')
#             break
#         except ValueError:
#             print('Введите числовое значение')
#             continue
# while True:
#     zapros()
#     povtor = input('\nХотите попробовать еще раз? (Да/Нет): ').strip().lower()
#     if povtor != 'да':
#         break

# print('До свиданья.\n')