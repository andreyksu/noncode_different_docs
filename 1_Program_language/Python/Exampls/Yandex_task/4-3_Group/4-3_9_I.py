def cycle(listt):
    i = 0
    lenn = len(listt)
    while True:
        yield listt[i % lenn]
        i += 1
    
print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))
print(*(x for _, x in zip(range(15), cycle([1, 2, 3, 4]))))

"""
Циклический генератор
Напишите генератор cycle, который принимает список и работает аналогично итератору itertools.cycle.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Пример 1
Ввод
    print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))
Вывод
    1 2 3 1 2

Пример 2
Ввод
    print(*(x for _, x in zip(range(15), cycle([1, 2, 3, 4]))))
Вывод
    1 2 3 4 1 2 3 4 1 2 3 4 1 2 3
"""