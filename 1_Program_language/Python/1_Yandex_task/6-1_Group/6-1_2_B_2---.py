import math

while True:
    listt = list()
    strr = input()
    if strr == "":
        for i in listt:
            print(math.gcd(*i))
        break
    tmpListt = strr.split(" ")
    tmpListtAsInt = [int(x) for x in tmpListt]
    listt.append(tmpListtAsInt)


from sys import stdin

lines = []
for line in stdin:
    lines.append(line.rstrip("\n"))
print(lines)

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
