from timeit import timeit
from sys import setrecursionlimit

setrecursionlimit(50_000)

def merge_sort(listt):
    if len(listt) == 1:
        return listt[:1]
    return append_in_place(merge_sort(listt[:1]), merge_sort(listt[1:]))
    # return append_in_place(merge_sort(listt[1:]), merge_sort(listt[:1]))  # Т.к. создаёт копию - потребляет память вёдрами.


def append_in_place(raw_list, sorted_list):
    for raw_item in raw_list:
        for position in range(len(sorted_list)):
            if sorted_list[position] < raw_item:
                continue
            else:
                sorted_list.insert(position, raw_item)
                break
        else:
            sorted_list.append(raw_item)
    return sorted_list

large_list =  [
           1000000, 1000, 500, -1, 4, 5, 6, 7, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2
        ]

print(merge_sort([7, 10, 6]))
print(merge_sort([7, 10, 6, 320, 1]))
print(merge_sort([3, 1, 5, 3]))
print(merge_sort(large_list))
print(f"Среднее время вычисления: "f"{round(timeit('merge_sort(large_list)', number=10, globals=globals()) / 10, 3)} с.")

"""
Сортировка слиянием
    Мы уже реализовывали функцию merge, которая способна "слить" два отсортированных списка в один.
    Чаще всего её применяют в рекурсивном алгоритме сортировки слиянием.

    Напишите рекурсивную функцию merge_sort, которая производит сортировку списка.

Примечание
    Ваше решение должно содержать только функции.
    В решении не должно быть вызовов требуемых функций, за исключением рекурсивных.
    Трассировка вызова рекурсивной функции в обработке ответа не учитывается и показана для примера.

Пример 1
Ввод
    result = merge_sort([3, 2, 1])
Вывод
    # Вызов merge_sort([3, 2, 1])
    # Вызов merge_sort([3])
    # Вызов merge_sort([2, 1])
    # Вызов merge_sort([2])
    # Вызов merge_sort([1])
    result = [1, 2, 3]

Пример 2
Ввод
    result = merge_sort([3, 1, 5, 3])
Вывод
    # Вызов merge_sort([3, 1, 5, 3])
    # Вызов merge_sort([3, 1])
    # Вызов merge_sort([3])
    # Вызов merge_sort([1])
    # Вызов merge_sort([5, 3])
    # Вызов merge_sort([5])
    # Вызов merge_sort([3])
    result = [1, 3, 3, 5]
"""