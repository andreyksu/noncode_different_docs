# Задача решена с учётом порядка подачи материала (методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

start_x = 0
start_y = 0

while True:
    target_str = input()
    if target_str == "СТОП":
        break
    step = int(input())
    if target_str == "СЕВЕР":
        start_x = start_x + step
    elif target_str == "ЮГ":
        start_x = start_x - step
    elif target_str == "ВОСТОК":
        start_y = start_y + step
    elif target_str == "ЗАПАД":
        start_y = start_y - step

print(start_x)
print(start_y)


"""
Маршрут построен
Навигация была важна во все времена.
Нам достался архив маршрутов движения, но их оказалось так много, что без автоматизации мы с ними не справимся вовек. Каждый маршрут представляет собой последовательность шагов в одном из четырех направлений:

СЕВЕР;
ВОСТОК;
ЮГ;
ЗАПАД.
Напишите программу, чтобы по заданному маршруту она определяла, в какой именно точке мы окажемся.
Для простоты будем считать, что в начале маршрута мы находимся в точке (0; 0).

Формат ввода
Вводятся инструкции маршрута в виде:
<направление>
<количество шагов>
Ввод завершается строкой СТОП.

Формат вывода
Два целых числа — координаты конечной точки маршрута.

Пример 1
    Ввод
        СЕВЕР
        2
        ВОСТОК
        2
        СТОП
    Вывод
        2
        2
Пример 2
    Ввод
        СЕВЕР
        2
        ЮГ
        3
        ЗАПАД
        4
        СТОП
    Вывод
    -1
    -4
"""
