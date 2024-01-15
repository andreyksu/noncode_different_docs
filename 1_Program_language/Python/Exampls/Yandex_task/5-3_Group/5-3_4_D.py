def only_positive_even_sum(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError

    if (a < 0 or b < 0) or (a % 2 != 0 or b % 2 != 0):
        raise ValueError

    return a + b

"""
Контроль параметров
Напишите функцию only_positive_even_sum, которая принимает два параметра и возвращает их сумму.

Если один из параметров не является целым числом, то следует вызвать исключение TypeError.
Если один из параметров не является положительным чётным числом, то следует вызвать исключение ValueError.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Пример 1
Ввод
    print(only_positive_even_sum("3", 2.5))
Вывод
    Вызвано исключение TypeError

Пример 2
Ввод
    print(only_positive_even_sum(-5, 4))
Вывод
    Вызвано исключение ValueError
"""
