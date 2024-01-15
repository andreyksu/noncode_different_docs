def merge(tuple_1, tuple_2):
    targetList = list()
    # targetList = addd(targetList, tuple_1)
    # targetList = addd(targetList, tuple_2)
    targetList = append_in_place(targetList, list(tuple_1))
    targetList = append_in_place(targetList, list(tuple_2))
    return tuple(targetList)


def addd(listt, tuplee):
    listLen = len(listt)
    if listLen == 0:
        return list(tuplee)
    for tup in tuplee:
        for postiton in range(len(listt)):
            if listt[postiton] < tup:
                continue
            else:                
                """
                # Это все заменить на listt.insert(position, tup)
                first_part = listt[:postiton]
                second_part = listt[postiton:]
                first_part.append(tup)
                listt = first_part + second_part
                """
                listt.insert(postiton, tup)
                break
        else:
            listt.append(tup)
    return listt


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

print(merge((1, 2), (3, 4, 5)))
print(merge((1, 7, 12, 50), (1, 9, 50)))

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