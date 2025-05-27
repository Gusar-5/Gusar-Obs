import calendar
y = int(input("Введите год: "))
if calendar.isleap(y):
    print("Год високосный")
else:
    print("Год не високосный")