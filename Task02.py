#Найти максимальное из пяти чисел
import random
a = int(random.randint(0, 10))
b = int(random.randint(0, 10))
c = int(random.randint(0, 10))
d = int(random.randint(0, 10))
e = int(random.randint(0, 10))
print(f"Первое число: {a}")
print(f"Второе число: {b}")
print(f"Третье число: {c}")
print(f"Четвертое число: {d}")
print(f"Пятое число: {e}")
max = a
if max < b:
    max = b
if max < c:
    max = c
if max < d:
    max = d
if max < e:
    max = e
print (f"Максимальное число {max}")