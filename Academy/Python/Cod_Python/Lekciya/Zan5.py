a = input('Введите текст: ')
print () # Делает Залавную а остальные строчные
print (a.lower()) # Делает Залавную а остальные строчные
print (a.capitalize()) # Делает Залавную а остальные строчные
print (a.title()) # Все слова с Заглавной
print (a.upper()) # Все слова с Заглавной
print ()
print (a[0])
print (a[-1])
b = a.find('д') 
if b == -1:
    print ('Такого символа не существует')
elif b >= 0: 
    print ()
    print (a.find('д'))     
    print (len(a) - a.rfind('д'))