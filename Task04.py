#Показать первую цифру дробной части числа
import random
a = random.random()
print(f"Введено число: {a}")
b = int((a*10)%10)
print(f"Первая цифра после точки: {b}")
