from timeit import timeit
from sys import setrecursionlimit

'''
Это решение тоже прошло в Яндексе. И по замерам, что яндекс предоставляет. Паять чуть чуть меньше потребовалась. Где на 1МБ где на 0.2МБ чем " 4-3_6_F_1---.py "
'''

setrecursionlimit(50_000)
# Это решение плохо тем что здесь есть глобальная переменная, которая собирает значения из всех запусков.

sorted_list = list() # Плохой варинат т.к. накапливает значение между запусками.... Если решить вопрос с очисткой при вычислении каждого нового списка - то как-то пойдёт. 
# Первый варинат: Через декоратор и внутри декоратора держать эту переменную???
# Второй вариант: Вложенный метод - рекурсия во внутреннем методое, а при вызове родительского лист обнуляется.

def merge_sort(raw_list):
    if len(raw_list) == 1:
        raw_item = raw_list[0]
        for position in range(len(sorted_list)):
            if sorted_list[position] < raw_item:
                continue
            else:
                sorted_list.insert(position, raw_item)
                break
        else:
            sorted_list.append(raw_item)
        return sorted_list
    if len(raw_list) > 1:
        # merge_sort(raw_list[:1]) # Убрал создание копии память перестала жраться вёдрами.
        # return merge_sort(raw_list[1:])
        merge_sort([raw_list.pop(0)])
        return merge_sort(raw_list)

large_list =  [
           1000000, 1000, 500, 4, 5, 6, 7, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2, 7, 10, 6, 320, 1, 3, 4, 3, 2
        ]

large_list *= 40
#print(merge_sort([7, 10, 6]))
#print(merge_sort([7, 10, 6, 320, 1]))
#print(merge_sort([3, 1, 5, 3]))
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