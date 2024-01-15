def merge(tuple_1, tuple_2):
    targetList = list()
    targetList += list(tuple_1)
    targetList += list(tuple_2)
    sortt(targetList)
    return tuple(targetList)


def sortt(listt):
    for i in range(len(listt)):
        for j in range(len(listt) - 1):
            if listt[j] > listt[j + 1]:
                listt[j], listt[j + 1] = listt[j + 1], listt[j]


print(merge((1, 2), (3, 4, 5)))
print(merge((7, 12), (1, 9, 50)))

"""
Слияние
Напишите функцию merge, которая принимает два отсортированных по возрастанию кортежа целых чисел, а возвращает один из всех переданных чисел.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.
В этой задаче отключены стандартные сортировки

Пример 1
Ввод
result = merge((1, 2), (3, 4, 5))
Вывод
result = (1, 2, 3, 4, 5)
Пример 2
Ввод
result = merge((7, 12), (1, 9, 50))
Вывод
result = (1, 7, 9, 12, 50)
"""