# Задача решена с учётом порядка подачи материала (методов итд, еще не было). Решал так если бы не знал перечисленного.

num_lines = int(input())

result_set_of_words = set()
for i in range(num_lines):
    target_str = input()
    list_of_words = target_str.split()
    result_set_of_words = result_set_of_words.union(set(list_of_words))

for i in result_set_of_words:
    print(i)


"""
Зайка — 8
Продолжаем считать заек за окном поезда.

Формат ввода
В первой строке записано натуральное число N — количество выделенных придорожных местностей.
В каждой из N последующих строк записано описание придорожной местности.

Формат вывода
Вывести все найденные объекты в придорожных местностях.

Пример 1
Ввод
3
березка елочка зайка волк березка
сосна зайка сосна елочка зайка медведь
сосна сосна сосна белочка сосна белочка
Вывод
сосна
березка
волк
елочка
медведь
белочка
зайка


Пример 2
Ввод
4
зайка березка
березка зайка
березка елочка березка
елочка елочка елочка
Вывод
березка
елочка
зайка
"""