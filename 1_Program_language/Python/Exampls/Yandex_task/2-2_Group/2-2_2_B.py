# Задача решена с учётом порядка подачи материала (циклов, методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

average_speed_Petr = int(input())
average_speed_Vasya = int(input())

if average_speed_Petr > average_speed_Vasya:
    print("Петя")
else:
    print("Вася")


'''
Кто быстрее?
В главной велогонке года участвует более тысячи гонщиков. Им предстоит пройти трассу длинной 43872м. Самая сложная и ответственная задача — определение победителя.

Нам известны средние скорости двух фаворитов — Пети и Васи. Помогите выяснить, кто из них пришёл к финишу первым.

Формат ввода
    В первой строке записана средняя скорость Пети.
    Во второй — Васи.

Формат вывода
    Имя победителя гонки.

Примечание
    Гарантируется, что победителем стал только один.

Пример 1
    Ввод
        10
        5
    Вывод
        Петя
'''