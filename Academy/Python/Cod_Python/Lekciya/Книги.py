book = ["Тир мушкетера", "Айвенго", "Целина", "Война и Мир"]

while True:
    main = int(input("Введите номер: \n"
                     "1 - Вывести список книг\n"
                     "2 - Добавить книгу в список\n"
                     "3 - Удалить книгу из списка\n"                    
                     "4 - Выход\n"))                    
                   
    if main not in [1, 2, 3, 4]:
        print ("Неправильный ввод")
        continue
    elif main == 1:
        if len(book) == 0:
            print("Cписок пуст\n")
            continue        
        print(book)
        continue
    elif main == 2:        
        v = input("Введите название книги: ")
        book.append(v)
        print("Книга добавлена\n")
        continue
    elif main == 3:
        if len(book) == 0:
            print("Cписок пуст\n")
            continue
        nom = int(input("Введите номер книги для удаления: ")) - 1        
        while nom >= len(book) or nom < 0:            
            print("Такой книги нет")
            nom = int(input("Введите номер книги для удаления: ")) - 1
        book.pop(nom)
        print("Книга удалена\n")           
        continue
    elif main == 4:
        break
       
