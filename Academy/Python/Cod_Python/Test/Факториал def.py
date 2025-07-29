def factorial(a):
    for i in range(1, a + 1):        
        a *= i
    return a
          
a = int(input('Введите число: '))
a = factorial(a)
print(f'Факториал равен: {a}')