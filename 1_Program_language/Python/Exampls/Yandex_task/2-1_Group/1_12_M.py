# Задача решена с учётом порядка подачи материала (циклов, методов, массивов/коллекций еще не было). Решал так если бы не знал перечисленного.

child_count = int(input())
swits_count = int(input())

count_for_each = swits_count // child_count
balance = swits_count - (count_for_each * child_count)

print(count_for_each)
print(balance)

"""
Дед Мороз и конфеты
    Настало самое главное событие в детском саду — новогодний утренник.
    Хорошо замаскированная робоняня в роли Деда Мороза решила раздать детям конфеты так, чтобы каждому досталось поровну. Напишите для робоняни алгоритм, который поможет распределить конфеты.

Формат ввода
    В первой строке указано количество детей на утреннике.
    Во второй строке — количество конфет в конфетном отсеке робоняни.

Формат вывода
    Сначала выведите количество конфет, которое выдано каждому ребенку, а затем количество конфет, что осталось в конфетном отсеке.

Пример 1
    Ввод
        3
        100
    Вывод
        33
        1
"""