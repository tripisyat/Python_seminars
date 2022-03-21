#Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

def is_true(x,y,z):
    expression1 = not (x or y or z)
    expression2 = not (x) and not (y) and not (z)
    return expression1 == expression2
signal=True


for x in range (0, 2):
    for y in range (0, 2):
        for z in range (0, 2):
            print (f'{x=}, {y=}, {z=}, result = {is_true(x,y,z)}')