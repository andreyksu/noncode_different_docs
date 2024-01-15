# Задача решена с учётом порядка подачи материала (циклов, методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

average_speed_Petr = int(input())
average_speed_Vasya = int(input())
average_speed_Tolya = int(input())

max_speed = max(average_speed_Petr, average_speed_Vasya, average_speed_Tolya)
min_speed = min(average_speed_Petr, average_speed_Vasya, average_speed_Tolya)

first = ""
second = ""
third = ""

Petr = "Петя"
Vasya = "Вася"
Tolya = "Толя"

if max_speed == average_speed_Petr: # Возможны проблемы на данных 1 1 2 и 2 2 1
    first = Petr
elif max_speed == average_speed_Vasya:
    first = Vasya
else:
    first = Tolya

if min_speed == average_speed_Petr:
    third = Petr
elif min_speed == average_speed_Vasya:
    third = Vasya
else:
    third = Tolya

if first != Petr and third != Petr:
    second = Petr
elif first != Vasya and third != Vasya:
    second = Vasya
else:
    second = Tolya

print(f"1. {first}")
print(f"2. {second}")
print(f"3. {third}")


"""
Список победителей
    Длина трассы — 43872м, и зрители хотят узнать имя победителя.

    Нам известны средние скорости трёх фаворитов – Пети, Васи и Толи. Помогите подвести итоги гонки.

Формат ввода
    В первой строке записана средняя скорость Пети.
    Во второй — Васи.
    В третьей — Толи.

Формат вывода
    Имена победителей в порядке занятых мест.

Пример 1
    Ввод
        10
        5
        7
    Вывод
        1. Петя
        2. Толя
        3. Вася
        
Пример 2
    Ввод
        5
        7
        10
    Вывод
        1. Толя
        2. Вася
        3. Петя
"""