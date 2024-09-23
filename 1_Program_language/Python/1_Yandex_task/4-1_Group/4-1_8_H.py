def is_palindrome(target):
    if isinstance(target, int):
        resultt = doWorkWithInt(target)
    elif isinstance(target, str):
        resultt = doWorkWithStr(target)
    elif isinstance(target, tuple):
        resultt = doWorkWithStr(target)
    elif isinstance(target, list):
        resultt = doWorkWithList(target)
    else:
        print("Missed target type")
    return resultt


def doWorkWithList(target):
    return verify(target)


def doWorkWithStr(target):
    return verify(list(target))


def doWorkWithTypel(target):
    return verify(list(target))


def doWorkWithInt(target):
    listt = list()
    listt.append(target % 10)
    target = target // 10
    while target >= 1:
        listt.append(target % 10)
        target = target // 10
    return verify(listt)


def verify(listt):
    listt = [str(i).lower() for i in listt]
    lenn = len(listt)
    if lenn == 0:
        return True
    fuze = lenn // 2
    for i in range(0, fuze + 1):
        if listt[i] != listt[i * (-1) - 1]:
            return False
    return True


print(doWorkWithInt(123))
"""
print("int-----" * 5)
print(is_palindrome(123))
print(is_palindrome(1))
print("str-----" * 5)
print(is_palindrome(""))
print(is_palindrome("dddddddddddddddddddddddddddd"))
print(is_palindrome("1w2W1"))
print(is_palindrome("1ww1"))
print(is_palindrome("1ww11"))
print("list-----" * 5)
print(is_palindrome([1, 2, 1, 2, 1]))
print(is_palindrome([1, 2, 1, 2, 2]))
print("tuple-----" * 5)
print(is_palindrome((1, 2, 1, 2, 1)))
print(is_palindrome((1, 2, 1, 2, 2)))
print(is_palindrome((1)))
print(is_palindrome(()))
"""

"""
А роза упала на лапу Азора 7.0
Напишите функцию is_palindrome, которая принимает натуральное число, строку, кортеж или список, а возвращает логическое значение: True — если передан палиндром, а в противном случае — False.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Для определения типа параметра можно воспользоваться функцией type или более продвинутой isinstance.

Пример 1
Ввод
result = is_palindrome(123)
Вывод
result = False
Пример 2
Ввод
result = is_palindrome([1, 2, 1, 2, 1])
Вывод
result = True
"""