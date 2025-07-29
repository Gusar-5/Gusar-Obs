# Вывод цифр в имени
s = input('\nВведите Имя: ').lower()
for i in range(ord('а'), ord('я') + 1):
    t = chr(i)
    if s.count(t) > 0:
         print(t, 'нашлось = ', s.count(t))

for i in range(ord('a'), ord('z') + 1):
    t = chr(i)
    if s.count(t) > 0:
        print(t, 'нашлось = ', s.count(t))