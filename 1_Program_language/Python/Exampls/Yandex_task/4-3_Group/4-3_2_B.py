def recursive_digit_sum(dig):
    if dig // 10 == 0:
        return dig
    else:
        return recursive_digit_sum(dig // 10) + dig % 10

result = recursive_digit_sum(123)
print(result)

result = recursive_digit_sum(7321346)
print(result)

"""
Рекурсивный сумматор цифр
Рекурсия – отличный способ избавиться от циклов, особенно от while. Давайте вспомним одну из наших старых задач и модернизируем её.

Напишите функцию recursive_digit_sum, которая находит сумму всех цифр натурального числа.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций, за исключением рекурсивных.
Трассировка вызова рекурсивной функции в обработке ответа не учитывается и показана для примера.

Пример 1
Ввод
result = recursive_digit_sum(123)
Вывод
# Вызов recursive_digit_sum(123)
# Вызов recursive_digit_sum(12)
# Вызов recursive_digit_sum(1)
# Вызов recursive_digit_sum(0)
result = 6
Пример 2
Ввод
result = recursive_digit_sum(7321346)
Вывод
# Вызов recursive_digit_sum(7321346)
# Вызов recursive_digit_sum(732134)
# Вызов recursive_digit_sum(73213)
# Вызов recursive_digit_sum(7321)
# Вызов recursive_digit_sum(732)
# Вызов recursive_digit_sum(73)
# Вызов recursive_digit_sum(7)
# Вызов recursive_digit_sum(0)
result = 26
"""