# Задача решена с учётом порядка подачи материала (методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

count_members = int(input())

maxx = 0
name_max = ""

for i in range(0, count_members):
    name = input()
    number = int(input())
    nextt = number
    tmp_summ = 0
    while nextt > 0:
        units = nextt % 10
        nextt = nextt // 10
        tmp_summ = tmp_summ + units
    else:
        if maxx <= tmp_summ:
            maxx = tmp_summ
            name_max = name

print(name_max)

"""
Максимальная сумма
Ребята в детском саду снова играют с числами. И пусть числа они знают плохо, придумывать их они очень любят.
Они договорились, что будут называть числа по очереди и тот, кто назовёт число с наибольшей суммой цифр, будет считаться победителем. В качестве судьи они выбрали бедную воспитательницу, и она попросила нас о помощи. Напишите программу, которая определит победителя.

Формат ввода
В первой строке записано число N — количество детей в группе. Далее вводятся имя ребенка и его число (каждое на своей строке).

Формат вывода
Требуется вывести имя победителя.
Если два ребенка назвали числа с одинаковой суммой цифр, победителем должен быть признан тот, кто ходил позже.

Пример 1
    Ввод
        2
        Аня
        123
        Боря
        234
    Вывод
        Боря
Пример 2
    Ввод
        3
        Аня
        1234
        Боря
        234
        Ваня
        2323
    Вывод
        Ваня
"""