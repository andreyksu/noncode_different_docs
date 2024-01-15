class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


listUpperCaseCyrillic = set()
listLowerCaseCyrillic = set()


def fillSetOfCahrs():
    A = "А"
    a = "а"
    E = "Ё"
    e = "ё"

    for i in range(ord(A), ord(A) + 32):
        listUpperCaseCyrillic.add(chr(i))

    for k in range(ord(a), ord(a) + 32):
        listLowerCaseCyrillic.add(chr(k))

    listUpperCaseCyrillic.add(E)
    listLowerCaseCyrillic.add(e)


def is_all_character_cyrillic(targetString):
    for i in targetString:
        if not ((i in listUpperCaseCyrillic) or (i in listLowerCaseCyrillic)):
            raise CyrillicError()


def is_first_char_is_upper(targetString):
    if not (targetString[0] in listUpperCaseCyrillic):
        raise CapitalError()


def is_upper_present_in_other_place(targetString):
    for i in range(len(targetString)):
        if i == 0:
            continue
        if targetString[i] in listUpperCaseCyrillic:
            raise CapitalError()


def name_validation(targetNameSurname):
    fillSetOfCahrs()
    if not (isinstance(targetNameSurname, str)):
        raise TypeError()
    is_all_character_cyrillic(targetNameSurname)
    is_first_char_is_upper(targetNameSurname)
    is_upper_present_in_other_place(targetNameSurname)
    return targetNameSurname


# print(name_validation("user"))
# print(name_validation("иванов"))
print(name_validation("Иванов"))
print(name_validation("ИваноВ"))

"""
Валидация имени
При регистрации в различных сервисах пользователи вводят большое количество информации. Правильное заполнение полей — важная часть работы программы, поэтому формы снабжают системами валидации данных.

Напишите функцию name_validation, которая принимает один позиционный аргумент — фамилию или имя.

Если параметр не является строкой, то вызовите исключение TypeError.

А также разработайте собственные ошибки:

CyrillicError — вызывается, если значение не состоит только из кириллических букв;
CapitalError — вызывается, если значение не начинается с заглавной буквы или найдена заглавная буква не в начале значения.
Обработка ошибок должна происходить в порядке, указанном в задании.

В случае успешного выполнения, функция должна вернуть переданный параметр без изменений.

Примечание
В решении не должно быть вызовов требуемых функций.

Пример 1
Ввод
    print(name_validation("user"))
Вывод
    Вызвано исключение CyrillicError
Пример 2
Ввод
    print(name_validation("иванов"))
Вывод
    Вызвано исключение CapitalError
"""
