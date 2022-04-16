#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и 
# записать в файл многочлен степени k. *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# k=3
# 6*x^3 + 4*x^2 + 7*x + 4 = 0
# 6*x^3 + 6*x^2 + 7 = 0

# k=6
# 2*x^6 + 8*x^5 + 7*x^4 + 6*x^3 + x^2 + 8 = 0
# 4*x^2 + 10*x + 10 = 0

# k=7
# 5*x^7 + 8*x^6 + 3*x^4 + 2*x^3 + 10*x^2 + 4*x + 2 = 0
# 1*x^2 + 5*x + 4 = 0

#k = 5
#Задачи 32, 33, 35, 36, 38, 39, 42, 43 в приоритете т к они попроще

# Вариант 1
# import random
# k = int(input('Введите k '))
# list1=[]
# for i in range(k):
#     y=random.randrange(0,100)
#     if y==0:
#         continue
#     else:
#         if i == 0:
#             list1.append(f"{y}")
#         else:
#             list1.append(f"{y}*X**{i}")
# list1.append(f"{random.randrange(1,100)}*X**{k}")
# print(list1)
# data = ""
# for i in range(-1,-(k+1), -1):
#     if i== -1:
#         data =data + list1[i]
#     else:
#         data =data + " + " + list1[i]
# result = f"k={k}=> {data} + {list1[0]} = 0"
# print(result)
# with open('PythonWelcome/Seminars/1st/Task033.txt', 'w') as file:
#     file.writelines(result)

import random
import itertools

k = random.randint(2,8)
print(f'{k}')

koefs = [random.randint(1,10) for i in range(k+1)]

def polinom(k, koefs):
    x_list = ['''*x^''']*(k-1)+['''*x''']
    print(x_list)
    polinomial = [[a,b,c] for a,b,c in itertools.zip_longest(koefs, x_list, range(k, 1, -1), fillvalue='')]
    
    for i in polinomial:
        i.append(' + ')

    print(f'{polinomial=}')
    result = list(itertools.chain(*polinomial))
    result = result[:-3]+['= 0']
    result=list(map(str,result))
    return ''.join(result)

answer = polinom(k, koefs)
print(answer)
