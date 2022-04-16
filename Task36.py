# 36 
# Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность.  
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.  
# Порядок элементов менять нельзя 

import random

list_example = [1, 5, 2, 3, 4, 6, 1, 7] 
n = len(list_example)
ind = 0
list_rise = [list_example[0]]
how_try = 0
while ind < n-1:
    how_try += 1
    ind2 = random.randint(ind, n-1)
    print(f'try:{how_try}; test_ind:{ind2}')
    if list_example[ind] < list_example[ind2]:
        list_rise.append(list_example[ind2])
        ind = ind2
print(list_rise)
