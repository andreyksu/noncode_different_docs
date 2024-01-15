def getENDict(num):
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    return months.get(num)


def getRUDict(num):
    months = {
        1: "Январь",
        2: "Февраль",
        3: "Март",
        4: "Апрель",
        5: "Май",
        6: "Июнь",
        7: "Июль",
        8: "Август",
        9: "Сентябрь",
        10: "Октябрь",
        11: "Ноябрь",
        12: "Декабрь",
    }
    return months.get(num)


def month(num, locale='ru'):
    if locale == "en":
        return getENDict(num)
    elif locale == "ru":
        return getRUDict(num)
    else:
        return ""

print(month(1, "en"))
print(month(1))
print(month(7, "ru"))

"""
Имя of the month 2.0
Разработайте функцию month, которая возвращает название заданного месяца с заглавной буквы. Функция должна принимать номер месяца и дополнительно обозначение языка (по умолчанию "ru").

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Пример 1
Ввод
result = month(1, "en")
Вывод
result = 'January'
Пример 2
Ввод
result = month(7)
Вывод
result = 'Июль'
"""