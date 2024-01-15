def is_prime(numm):
    if numm < 4:
        return True
    limit = int(numm ** (1 / 2))
    for i in range(2, limit + 1):
        if numm % i == 0:
            return False
    else:
        return True


print(is_prime(1001459))
print(is_prime(79701))

"""
Простая задача 5.0
Напишите функцию is_prime, которая принимает натуральное число, а возвращает булево значение: True — если переданное число простое, а иначе — False.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Пример 1
Ввод
result = is_prime(1001459)
Вывод
result = True
Пример 2
Ввод
result = is_prime(79701)
Вывод
result = False
"""