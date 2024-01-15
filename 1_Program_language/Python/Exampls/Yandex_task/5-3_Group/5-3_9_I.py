class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def name_validation(targetNameSurname):

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
        for i in range(1, len(targetString)):
            if targetString[i] in listUpperCaseCyrillic:
                raise CapitalError()

    fillSetOfCahrs()
    if not (isinstance(targetNameSurname, str)):
        raise TypeError()
    is_all_character_cyrillic(targetNameSurname)
    is_first_char_is_upper(targetNameSurname)
    is_upper_present_in_other_place(targetNameSurname)
    return targetNameSurname


def username_validation(targetNameSurname):

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

    fillSetOfCahrs()
    if not (isinstance(targetNameSurname, str)):
        raise TypeError()
    is_all_character_lat(targetNameSurname)
    is_first_char_is_number(targetNameSurname)
    return targetNameSurname


def user_validation(**kwargs):
    listtOfNamedArgs = ["last_name", "first_name", "username"]
    listGotArgs = kwargs.keys()

    if len(listGotArgs) != 3:
        raise KeyError()

    for i in listtOfNamedArgs:
        if not (i in listGotArgs):
            raise KeyError()

    for i in listtOfNamedArgs:
        if not (isinstance(kwargs[i], str)):
            raise TypeError()

    name_validation(kwargs["last_name"])
    name_validation(kwargs["first_name"])
    username_validation(kwargs["username"])

    return kwargs


print(user_validation(last_name="Иванов", first_name="Иван", username="ivanych45"))
print(
    user_validation(
        last_name="Иванов", first_name="Иван", username="ivanych45", password="123456"
    )
)

"""
Это решение прошло проверку. Ничего не менял, просто вытащил из классов и засунул во внешние в методы.

Валидация пользователя
Используйте две предыдущих функции валидации и напишите функцию user_validation, которая принимает именованныеаргументы:

last_name — фамилия;
first_name — имя;
username — имя пользователя.
Если функции был передан неизвестный параметр или не передан один из обязательных, то вызовите исключение KeyError.

Если один из параметров не является строкой, то вызовите исключение TypeError.

Обработка данных должна происходить в порядке: фамилия, имя, имя пользователя.

Если поле заполнено верно, функция возвращает словарь с данными пользователя.

Примечание
В решении не должно быть вызовов требуемых функций.

Пример 1
Ввод
print(user_validation(last_name="Иванов", first_name="Иван", username="ivanych45"))
Вывод
{'last_name': 'Иванов', 'first_name': 'Иван', 'username': 'ivanych45'}
Пример 2
Ввод
print(user_validation(last_name="Иванов", first_name="Иван", username="ivanych45", password="123456"))
Вывод
Вызвано исключение KeyError
"""
