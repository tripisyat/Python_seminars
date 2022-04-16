#Составить список простых множителей натурального числа N
# 31 Составить список простых множителей натурального числа N
# 1 вариант все делители числа N
# def Multipliers_for(n):
#     multi_list = []
#     for i in range(n):
#         for j in range(i, n):
#             element = []
#             if i * j == n:
#                 element.append([i, j])
#                 multi_list.extend(element)
#     return multi_list

# n = 30 #int(input())
# print(*Multipliers_for(n))

# 2 вариант правильный!
# n = int(input("Введите натуральное число: "))
# def factorization(n):
#     factors = list()
#     divisor = 2
#     while(divisor <= n):
#         if (n % divisor) == 0:
#             factors.append(divisor)
#             n = n/divisor
#         else:
#             divisor += 1
#     return factors
# print(factorization(n))

# решето эратосвена
# def eratosthenes(n):     # n - число, до которого хотим найти простые числа 
#     sieve = list(range(n + 1))
#     sieve[1] = 0    # без этой строки итоговый список будет содержать единицу
#     for i in sieve:
#         if i > 1:
#             for j in range(2*i, len(sieve), i):
#                 sieve[j] = 0
#     return set(sieve) # set переводит в множества,при этом удалит ненужные нули
# print()


# Самое верное решение))

n = int(input("Введите натуральное число: "))
list = []
for i in range (2, n):
    while n%i==0:
        n/=i
        list.append(i)
print(list)