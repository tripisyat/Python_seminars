#Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
#Т е для k = 8, список будет выглядеть так: [-21 , 13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def negafib(n): 
    if n in [-1,0,1]: 
        return abs(n) # возвращаем по модулю
    elif n < 0: 
        n = abs(n) 
        return (-1)**(n+1)*(negafib(n-1)+negafib(n-2)) # формула отрицательного Фибоначчи
    else: 
        return negafib(n-1)+negafib(n-2) 
 
n = int(input('Введите число n = ')) 

list = [] 
for i in range(-n,n+1): 
    list.append(negafib(i)) 
print(list)