#Найти сумму чисел списка стоящих на нечетной позиции
spisok = [1,2,3,4]
sumSpisok = 0
for i in range(len(spisok)):
    if i%2 !=0:
        sumSpisok=sumSpisok+spisok[i]
print(sumSpisok)