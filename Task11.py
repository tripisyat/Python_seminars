#Сформировать список из  N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.
# n = int(input('Введите число: '))

# def get_degree(n):
#     return [((-3)**i) for i in range(n)]

# print (get_degree(n))

num = int(input('Введите число: '))
N = []
n=1
for i in range(num):
    N.append(n)
    n=n*(-3)
print(N)