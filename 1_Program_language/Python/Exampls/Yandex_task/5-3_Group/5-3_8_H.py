class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


listUpperCase = set()
listLowerCase = set()
listOfDigital = set()
additionalList = set()


def fillSetOfCahrs():
    A = "A"
    a = "a"
    under = "_"

    for i in range(ord(A), ord(A) + 26):
        listUpperCase.add(chr(i))

    for k in range(ord(a), ord(a) + 26):
        listLowerCase.add(chr(k))

    for z in range(0, 10):
        listOfDigital.add(f"{z}")

    additionalList.add(under)


def is_all_character_lat(targetString):
    for i in targetString:
        if not (
            (i in listUpperCase)
            or (i in listLowerCase)
            or (i in listOfDigital)
            or (i in additionalList)
        ):
            raise BadCharacterError()


def is_first_char_is_number(targetString):
    if targetString[0] in listOfDigital:
        raise StartsWithDigitError()


def username_validation(targetNameSurname):
    fillSetOfCahrs()
    if not (isinstance(targetNameSurname, str)):
        raise TypeError()
    is_all_character_lat(targetNameSurname)
    is_first_char_is_number(targetNameSurname)
    return targetNameSurname


# print(username_validation("$user_45$"))
# print(username_validation("45_user"))
print(username_validation("s45_user"))

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
