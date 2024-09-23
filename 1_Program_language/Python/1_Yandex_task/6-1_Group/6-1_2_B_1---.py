import math

listt = list()

while (strr := input()) != "":
    tmpListt = strr.split(" ")
    tmpListtAsInt = [int(x) for x in tmpListt]
    listt.append(tmpListtAsInt)

while True:
    strr = input()
    if strr == "":
        break
    tmpListt = strr.split(" ")
    tmpListtAsInt = [int(x) for x in tmpListt]
    listt.append(tmpListtAsInt)

for i in listt:
    print(math.gcd(*i))


"""
Решение не подходило. Т.к. нужно было через stdin.

Потоковый НОД
Напишите программу, находящую наибольшие общие делители для всех переданных в стандартный поток последовательностей чисел.

Формат ввода
Вводятся строки чисел, разделённых пробелами.

Формат вывода
Последовательность чисел — наибольшие общие делители всех последовательностей.

Пример
Ввод
    2 1000 20 34
    36 12
    3 96 12
    6
    7 8 9 10
Вывод
    2
    12
    3
    6
    1
"""
