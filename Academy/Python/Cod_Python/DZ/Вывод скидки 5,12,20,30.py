while True:
    print("Вывод скидки")
    x = int(input("Введите сумму: "))
    if x <= 0:
        print(f"Ввод не коректных данных попробуйте снова\n")  
    elif x <= 5000:
        x1 = x *.05
        print(f"Ваща скидка 5% и составляет: {x1:.0f}. Cумма к оплате {x - x1:.0f}\n")
    elif 5000 < x <= 15000:
       x1 = x * .12
       print(f"Ваща скидка 12% и составляет: {x1:.0f}. Cумма к оплате {x - x1:.0f}\n")
    elif 15000 < x <= 25000:
        x1 = x * .2
        print(f"Ваща скидка 20% и составляет: {x1:.0f}. Cумма к оплате {x - x1:.0f}\n")
    elif x > 25000:
        x1 = x * .3
        print(f"Ваща скидка 30% и составляет: {x1:.0f}. Cумма к оплате {x - x1:.0f}\n")
    