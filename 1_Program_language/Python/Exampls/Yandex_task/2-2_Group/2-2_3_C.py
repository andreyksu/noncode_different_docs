# Задача решена с учётом порядка подачи материала (циклов, методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

average_speed_Petr = int(input())
average_speed_Vasya = int(input())
average_speed_Tolya = int(input())

max_speed = max(average_speed_Petr, average_speed_Vasya, average_speed_Tolya)

if max_speed == average_speed_Petr:
    print("Петя")
elif max_speed == average_speed_Vasya:
    print("Вася")
else:
    print("Толя")

'''
Кто быстрее на этот раз?
    Вновь велогонщики собрались узнать, кто из них быстрее. Им предстоит пройти трассу длиной 43872м, и нам нужно вновь определить победителя.

    На этот раз нам известны средние скорости трёх фаворитов — Пети, Васи и Толи. Кто из них пришёл к финишу первым?

Формат ввода
    В первой строке записана средняя скорость Пети.
    Во второй — Васи.
    В третьей — Толи.

Формат вывода
    Имя победителя гонки.

Примечание
    Гарантируется, что победителем стал только один.

Пример 1
    Ввод
        10
        5
        7
    Вывод
        Петя
'''