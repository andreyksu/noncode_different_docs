"""
Это решение не нравится тем, что каждый раз создаётся новый списко. Первое - это время на создание нового списка, второе это хранение в памяти.
Хотя при запуске в Яндексе - различий не замечено в части потребвения памяит - при сравнении запуска обоих видов.
"""


def make_linear(raw_of_list, target_list=None):
    print(f"raw_of_list = {raw_of_list} target_list = {target_list}")
    # if not target_list: # Плохо. Если список пустой то он в логическом выражении является False. Т.е. not False даст true.
    if target_list is None:
        target_list = list()
    for inst in raw_of_list:
        if isinstance(inst, list):
            tmp_list = make_linear(inst)
            target_list += tmp_list
        else:
            target_list.append(inst)
    return target_list


"""
Здесь вроде как уменьшение потребления памяти, но по факту при запуске в Яндексе - параметры потребления схожие с первым решением.
Видимо списки не очень большие.
"""


def make_linear_1(raw_of_list, target_list=None):
    if target_list is None:
        target_list = list()
    for inst in raw_of_list:
        if isinstance(inst, list):
            make_linear_1(inst, target_list)
        else:
            target_list.append(inst)
    return target_list


"""
result = make_linear([1, 2, [3]])
print(result)
result = make_linear([1, [2, [3, 4]], 5, 6])
print(result)
result = make_linear([[3], 1, [2, [3, [4, [3]], [5]]], 5, 6])
print(result)
result = make_linear([[[[[1]]]]])
print(result)
"""

"""
result = make_linear_1([1, 2, [3]])
print(result)
result = make_linear_1([1, [2, [3, 4]], 5, 6])
print(result)
result = make_linear_1([[3], 1, [2, [3, [4, [3]], [5]]], 5, 6])
print(result)
"""
result = make_linear([[[[[[1]]]]], [[[[[1]]]]]])
print(result)
result = make_linear_1([[[[[[1]]]]], [[[[[1]]]]]]) # На этой проверке была ошибка. Т.к. была проверка "if not target_list" а пустой списко есть False. А нужно проверять "if targe_list is None"
print(result)

"""
"Выпрямление" списка
Весьма часто, данные, которые мы получаем из различных источников, не удовлетворяют нашим пожеланиям. Одна из частых проблем – излишняя вложенность списков.

Напишите функцию make_linear, которая принимает список списков и возвращает его "выпрямленное" представление.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций, за исключением рекурсивных.
Трассировка вызова рекурсивной функции в обработке ответа не учитывается и показана для примера.

Пример 1
Ввод
    result = make_linear([1, 2, [3]])
Вывод
    # Вызов make_linear([1, 2, [3]])
    # Вызов make_linear([3])
    result = [1, 2, 3]

Пример 2
Ввод
    result = make_linear([1, [2, [3, 4]], 5, 6])
Вывод
    # Вызов make_linear([1, [2, [3, 4]], 5, 6])
    # Вызов make_linear([2, [3, 4]])
    # Вызов make_linear([3, 4])
    result = [1, 2, 3, 4, 5, 6]
"""