#По двум заданным числам проверить является ли одно квадратом второго

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a*a == b:
    print (f'Число {b} является квадратом числа {a}') 
else:
    print (f'Число {b} не является квадратом числа {a}')