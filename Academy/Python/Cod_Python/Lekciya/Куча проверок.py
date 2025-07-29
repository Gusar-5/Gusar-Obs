'''
Поиск всех маленьких англ букв - string.ascii_lowercase
Поиск всех Больших англ букв - string.ascii_uppercase
Поиск всех англ букв - string.ascii_letters
Поиск всех симолы англ - string.printable

'''

# Вывод цифр в имени
import string

s = input('\nВведите Имя: ').lower()
for i in range(ord('а'), ord('я') + 1):
    t = chr(i)
    if s.count(t) > 0:
         print(t, 'нашлось = ', s.count(t))
print()

for i in range(ord('a'), ord('z') + 1):
    t = chr(i)
    if s.count(t) > 0:
        print(t, 'нашлось = ', s.count(t))
print()

for i in string.punctuation: # Проверка символов
    if s.count(i) > 0:
        print(i, 'нашлось = ', s.count(i))
print()

for i in string.digits: # Подлкбчена цифр
    if s.count(i) > 0:
        print(i, 'нашлось = ', s.count(i))
print()

for i in string.whitespace: # Подлкбчена Пробелов
    if s.count(i) > 0:
        print('Пробелов нашлось = ', s.count(i))
print()