# Задача решена с учётом порядка подачи материала (методов, еще не было. По коллекциям дали только что list). Решал так если бы не знал перечисленного.

input_lint = input()

listt = input_lint.split(" ")
for i in range(0, len(listt)):
    listt[i] = int(listt[i])

listt.sort()

lenn = len(listt)
nod = None
first = None
second = None
if lenn > 1:
    first = listt[0]
    second = listt[1]
    fuzze = True
else:
    nod = listt[0]
    fuzze = False

while fuzze:
    tmp = second % first
    if tmp == 0:
        nod = first
        fuzze = False
    elif tmp == 1:
        nod = 1
        fuzze = False
    else:
        second = first
        first = tmp

for i in range(1, lenn):
    if listt[i] % nod != 0:
        nod = 1
        break

print(nod)


"""
НОД 3.0
Местному НИИ в очередной раз нужно находить наибольший общий делитель (НОД) нескольких чисел.
Руководство института вернулось с этой задачей к нам.

Формат ввода
В единственной строке записывается последовательность натуральных чисел, разделённых пробелами.

Формат вывода
Требуется вывести одно натуральное число — НОД всех данных чисел.

Примечание
Самый распространенный способ поиска НОД — Алгоритм Эвклида.

Пример 1
    Ввод
    12 42
    Вывод
    6
Пример 2
    Ввод
    102 39 768
    Вывод
    3
"""