def number_length(target):
    temp_result = str(target).strip("+-")
    return len(temp_result)

print(number_length(12345))
print(number_length(-100500))
print(number_length(+100500))

"""
Длина числа
Разработайте функцию number_length, которая принимает одно целое число и возвращает его длину без учёта знака.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Пример 1
Ввод
result = number_length(12345)
Вывод
result = 5
Пример 2
Ввод
result = number_length(-100500)
Вывод
result = 6
"""