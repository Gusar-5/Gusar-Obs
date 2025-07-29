import string

while True:
    a = input('\nВведите пароль: ')
    if len(a) != 8:
        print('Пароль должен быть из 8 символов')
        continue
    if ' ' in a:
        print('Пароль должен быть без пробелов')
        continue   
    proverka = False
    for i in a:
        if i in string.ascii_uppercase:
            proverka = True
            break
    if not proverka:
        print('В пароле должна быть минимум 1 заглавная буква')
        continue

    proverka = False
    for i in a:
        if i in string.punctuation:
            proverka = True
            break
    if not proverka:
        print('В пароле должен быть минимум 1 знак')
        continue
    
    count = 0
    for i in a:
        if i in string.ascii_lowercase:
            count += 1
    if count < 2:
        print('В пароле должно быть минимум 2 строчные буквы')
        continue

    count_c = 0
    for i in a:
        if i.isdigit():
            count_c += 1
    if count_c < 3:
        print('В пароле должно быть минимум 3 цифры')
        continue
    
    print(f'Пароль {a} соответсвует\n')
    break