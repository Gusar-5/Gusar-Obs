import random
x = list(range(101))
print("\nВывод рандомного числа из списка")
for i in range(10):
    n = random.choice(x)
    print("\t", n)