# массив, кортеж, дек и множество
import random
import array
import time
from collections import deque

s1 = []
s2 = []

for i in range(5): # Формируем в списках по 5 случайных чисел
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    s1.append(a)
    s2.append(b)

print(f'\nСоздали 2 разных списка:\n{s1}, {s2}'), time.sleep(4)

# Объединяем списки
s = s1 + s2
print(f'\nОбъединили списки в один список:\n{s}'), time.sleep(4)

# Преобразуем в deque
s = deque(s)

# Добавляем 1 слева и справа
s.append(1)        
s.appendleft(1)    

print(f'\nСформировали дек, и добавили 1 слева и справа:\n{s}'), time.sleep(4)
# Формируем множество
m = set(s)
print(f'\nСформировали множество:\n{list(m)}'), time.sleep(4)
# Формируем массив
y = list(set(s1) & set(s2)) # использование оператора & (пересечение)
s = array.array('i', y)
print(f'\nСформировали массив содержащий общие элементы для 1 и 2 списка:\n{list(s)}'), time.sleep(4)
# Формируем список уникальных элементв
u = u = list(set(s1 + s2))
print(f'\nСформировали список уникальных элементв 1 и 2 списков:\n{list(u)}'), time.sleep(4)
# Формируем кортеж
s = (max(s1), min(s1), max(s2), min(s2))
print(f'\nСформировали кортеж из MIN и MAX каждого из списков:\n{list(s)}')