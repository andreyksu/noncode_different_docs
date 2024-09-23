def gcd(first, second):
    maxx = max(first, second)
    minn = min(first, second)

    target = minn
    while target > 0:
        if minn % target == 0 and maxx % target == 0:
            return target
        else:
            target -= 1


# result = gcd(12, 45)
# print(result)
# result = gcd(144, 96)
# print(result)


"""
Функциональный НОД
Напишите функцию gcd, которая принимает два натуральных числа и возвращает их наибольший общий делитель.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Пример 1
Ввод
result = gcd(12, 45)
Вывод
result = 3
Пример 2
Ввод
result = gcd(144, 96)
Вывод
result = 48
"""