#Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности


list = [1, 2, 3, 5, 1, 5, 3, 10]

def number(list):
    unnumber = []
    for number in list:
        if number in unnumber:
            continue
        else:
            unnumber.append(number)
    return unnumber

print(number(list))
