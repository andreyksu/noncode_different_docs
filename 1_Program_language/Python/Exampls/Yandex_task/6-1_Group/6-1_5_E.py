import math


first = input()
second = input()

splitedFirst = first.split(" ")
splitedSecond = second.split(" ")

firstPoints = [float(i) for i in splitedFirst]
floatSecondList = [float(i) for i in splitedSecond]

secondPoints = list()
secondPoints.append(math.cos(floatSecondList[1]) * floatSecondList[0])
secondPoints.append(math.sin(floatSecondList[1]) * floatSecondList[0])
print(firstPoints, secondPoints)
print(math.dist(firstPoints, secondPoints))


"""
Шаг навстречу
Два выдуманных человечка Дека и Поля, пользуются каждый своей системой координат. Деке нравится представлять себя в декартовом пространстве, а Поле — в полярном.

Напишите программу, определяющую кратчайшее расстояние, которое нужно пройти Деке и Поле, чтобы встретиться.

Формат ввода
В первой строке записаны координаты Деки: два рациональных числа — x и y
Во второй строке записаны координаты Поли: два рациональных числа — ρ и ϕ

Формат вывода
Одно число — расстояние между Декой и Полей.

Примечание
Дека и Поля живут на одной плоскости с общим центром.

𝜙
ϕ — измеряется в радианах.
"""
