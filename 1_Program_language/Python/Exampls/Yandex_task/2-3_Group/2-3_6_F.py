# Задача решена с учётом порядка подачи материала (методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

first = int(input())
second = int(input())

minn = min(first, second)
nod = 1

for i in range(minn, 1, -1):
    if first % i == 0 and second % i == 0:
        nod = i
        break

print(nod)

"""
НОД
В одном из местных НИИ часто требуется находить наибольший общий делитель (НОД) двух чисел.
Вам уже доверяют, как одному из лучших «автоматизаторов» в округе, так что руководство НИИ решило заказать ПО у вас.

Формат ввода
Вводится два натуральных числа, каждое на своей строке.

Формат вывода
Требуется вывести одно натуральное число — НОД двух данных чисел.

Примечание
Самый распространенный способ поиска НОД — алгоритм Евклида.

Пример 1
    Ввод
        12
        42
    Вывод
        6
Пример 2
    Ввод
        512
        625
    Вывод
        1
"""