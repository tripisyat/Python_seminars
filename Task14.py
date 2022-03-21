#Подсчитать сумму цифр в вещественном числе.
import random
num = random.randint(0,1000)
numOrig = num
print(f'Выпало число: {num}')
sum=0
while num!=0:
    sum=sum+num%10
    num//=10
print(f'Сумма цифр в числе {numOrig} равно: {sum}')