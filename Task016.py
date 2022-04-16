#Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму

import random #подключение модуля случайных чисел random
print('Введите границы диапазона:')
border1 = int(input())
border2 = int(input())
array = []*10
for i in range(0,11):
  array[i] = random.randint(border1, border2)
print(array)