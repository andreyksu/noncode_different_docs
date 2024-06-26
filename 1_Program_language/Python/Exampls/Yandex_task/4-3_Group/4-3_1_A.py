def recursive_sum(*arr):
    if len(arr) == 1:
        return arr[0]
    return recursive_sum(*arr[1:]) + arr[0]



result = recursive_sum(1, 2, 3)
print(result)

result = recursive_sum(7, 1, 3, 2, 10)
print(result)

"""
Рекурсивный сумматор
Большинство задач этой главы ориентировано на отработку навыков по разработке рекурсивных функций.

Ваше решение будет использоваться как библиотека.

Напишите функцию recursive_sum, которая находит сумму всех позиционных аргументов.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций, за исключением рекурсивных.
Трассировка вызова рекурсивной функции в обработке ответа не учитывается и показана для примера.

Пример 1
Ввод
result = recursive_sum(1, 2, 3)
Вывод
# Вызов recursive_sum(1, 2, 3)
# Вызов recursive_sum(1, 2)
# Вызов recursive_sum(1)
# Вызов recursive_sum()
result = 6
Пример 2
Ввод
result = recursive_sum(7, 1, 3, 2, 10)
Вывод
# Вызов recursive_sum(7, 1, 3, 2, 10)
# Вызов recursive_sum(7, 1, 3, 2)
# Вызов recursive_sum(7, 1, 3)
# Вызов recursive_sum(7, 1)
# Вызов recursive_sum(7)
# Вызов recursive_sum()
result = 23
"""