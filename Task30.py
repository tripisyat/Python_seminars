#Вычислить число Пи c заданной точностью d
import math
def round_pi(d):
    if 0.1>=d>=10**-10: #ограничиваем диапазон
        for_round = len(str(d))-2 # переводим в строку и считаем количество
        pi = math.pi
        new_pi = round(pi, for_round )
    else:
        new_pi = 'd не в заданном диапазоне'
    return new_pi


d=0.0001# int(input('Введите коэффициент точности от 10**-1 до 10**-10'))

print(round_pi(d))

