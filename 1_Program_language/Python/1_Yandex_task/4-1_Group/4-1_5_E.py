def split_numbers(numbers_as_str):
    numbers_as_list = numbers_as_str.split()
    res_numbers_as_list = [int(num) for num in numbers_as_list]
    return tuple(res_numbers_as_list)

print(split_numbers("1 2 3 4 5"))
print(split_numbers("1 -2 3 -4 5"))

"""
Числовая строка
Разработайте функцию split_numbers, которая принимает строку целых чисел, разделённых пробелами, и возвращает кортеж из этих чисел.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Вы можете спросить: почему кортеж, а не список. Всё дело в безопасности. Кортежи неизменяемые коллекции и их безопаснее передавать в функцию или из неё.

Пример 1
Ввод
result = split_numbers("1 2 3 4 5")
Вывод
result = (1, 2, 3, 4, 5)
Пример 2
Ввод
result = split_numbers("1 -2 3 -4 5")
Вывод
result = (1, -2, 3, -4, 5)
"""