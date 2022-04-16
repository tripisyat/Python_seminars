#Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 
import math
lst = [1,2,3]
res_lst = []
len_res_lst = math.ceil(len(lst)/2)
temp=0

for i, x in enumerate(lst):
    if len(res_lst) != len_res_lst:
        