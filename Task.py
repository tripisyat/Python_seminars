#Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
n = int(input('Введите число: '))
def fib(n):
 if n in [1, 2]:
    return 1
 else:
    return fib(n-1) + fib(n-2)

list = []
for i in range(1,n+1):
    list.append(fib(i))

print(list)