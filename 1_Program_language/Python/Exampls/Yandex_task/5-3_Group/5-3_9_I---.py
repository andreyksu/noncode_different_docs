class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


class WirifyTheName:

    listUpperCaseCyrillic = set()
    listLowerCaseCyrillic = set()

    @classmethod
    def fillSetOfCahrs(cls):
        A = "А"
        a = "а"
        E = "Ё"
        e = "ё"

        for i in range(ord(A), ord(A) + 32):
            cls.listUpperCaseCyrillic.add(chr(i))

        for k in range(ord(a), ord(a) + 32):
            cls.listLowerCaseCyrillic.add(chr(k))

        cls.listUpperCaseCyrillic.add(E)
        cls.listLowerCaseCyrillic.add(e)

    @classmethod
    def is_all_character_cyrillic(cls, targetString):
        for i in targetString:
            if not (
                (i in cls.listUpperCaseCyrillic) or (i in cls.listLowerCaseCyrillic)
            ):
                raise CyrillicError()

    @classmethod
    def is_first_char_is_upper(cls, targetString):
        if not (targetString[0] in cls.listUpperCaseCyrillic):
            raise CapitalError()

    @classmethod
    def is_upper_present_in_other_place(cls, targetString):
        for i in range(len(targetString)):
            if i == 0:
                continue
            if targetString[i] in cls.listUpperCaseCyrillic:
                raise CapitalError()

    @classmethod
    def name_validation(cls, targetNameSurname):
        cls.fillSetOfCahrs()
        if not (isinstance(targetNameSurname, str)):
            raise TypeError()
        cls.is_all_character_cyrillic(targetNameSurname)
        cls.is_first_char_is_upper(targetNameSurname)
        cls.is_upper_present_in_other_place(targetNameSurname)
        return targetNameSurname


class WirifyTheUsername:

    listUpperCase = set()
    listLowerCase = set()
    listOfDigital = set()
    additionalList = set()

    @classmethod
    def fillSetOfCahrs(cls):
        A = "A"
        a = "a"
        under = "_"

        for i in range(ord(A), ord(A) + 26):
            cls.listUpperCase.add(chr(i))

        for k in range(ord(a), ord(a) + 26):
            cls.listLowerCase.add(chr(k))

        for z in range(0, 10):
            cls.listOfDigital.add(f"{z}")

        cls.additionalList.add(under)

    @classmethod
    def is_all_character_lat(cls, targetString):
        for i in targetString:
            if not (
                (i in cls.listUpperCase)
                or (i in cls.listLowerCase)
                or (i in cls.listOfDigital)
                or (i in cls.additionalList)
            ):
                raise BadCharacterError()

    @classmethod
    def is_first_char_is_number(cls, targetString):
        if targetString[0] in cls.listOfDigital:
            raise StartsWithDigitError()

    @classmethod
    def username_validation(cls, targetNameSurname):
        cls.fillSetOfCahrs()
        if not (isinstance(targetNameSurname, str)):
            raise TypeError()
        cls.is_all_character_lat(targetNameSurname)
        cls.is_first_char_is_number(targetNameSurname)
        return targetNameSurname


name_validation = WirifyTheName.name_validation
username_validation = WirifyTheUsername.username_validation


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
Это решение НЕ прошло проверку. В отличии от решения что прошло проверку, здесь отличие только в том что всё находится в классах. А в прошедшем проверку, все во внешней функции.

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
