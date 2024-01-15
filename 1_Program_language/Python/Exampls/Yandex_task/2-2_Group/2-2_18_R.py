# Задача решена с учётом порядка подачи материала (циклов, методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

a = int(input())
b = int(input())
c = int(input())

max = max(a, b, c)
min = min(a, b, c)

middle = (a + b + c) - (min + max)

if max**2 == middle**2 + min**2:
    print("100%")
elif max**2 > middle**2 + min**2:
    print("велика")
else:
    print("крайне мала")


"""
Территория зла
В давние времена считалось, что если какая-то местность является треугольником, то в ней заключено страшное зло.

При этом люди оценивали риск встретить зло по форме этого треугольника:

в остроугольном треугольнике вероятность встретить зло крайне мала;
в тупоугольном — велика;
в прямоугольном — 100%.
Напишите программу, которая по длине сторон треугольной местности, определяет вероятность встретить зло.

Формат ввода
Три числа — длины сторон треугольной местности.

Формат вывода
Вероятность встретить зло согласно поверью:

крайне мала;
велика;
100%.
Пример 1
    Ввод
        3
        5
        4
    Вывод
        100%
Пример 2
    Ввод
        6
        3
        4
    Вывод
        велика
"""
