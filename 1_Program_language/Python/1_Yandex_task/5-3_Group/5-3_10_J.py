import hashlib


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(
    passwd, min_length=8, possible_chars="", at_least_one=str.isdigit
):

    def fillSetOfCahrs():
        defaultSetOfChars = set()
        A = "A"
        a = "a"

        for i in range(ord(A), ord(A) + 26):
            defaultSetOfChars.add(chr(i))

        for k in range(ord(a), ord(a) + 26):
            defaultSetOfChars.add(chr(k))

        for z in range(0, 10):
            defaultSetOfChars.add(f"{z}")

        return defaultSetOfChars

    possible_chars_inner = ""
    if possible_chars == "":
        possible_chars_inner = fillSetOfCahrs()
    else:
        possible_chars_inner = possible_chars
    if not isinstance(passwd, str):
        raise TypeError()
    if len(passwd) < min_length:
        raise MinLengthError()
    for i in passwd:
        if i not in possible_chars_inner:
            raise PossibleCharError()
    isContainsMandatoryChar = False
    for i in passwd:
        isContainsMandatoryChar = isContainsMandatoryChar or at_least_one(i)
    if not isContainsMandatoryChar:
        raise NeedCharError()

    return hashlib.sha256(str.encode(passwd)).hexdigest()


print(password_validation("Hello12345"))

print(
    password_validation(
        "$uNri$e_777", min_length=6, at_least_one=lambda char: char in "!@#$%^&*()_"
    )
)

"""
Валидация пароля
После того как пользователь ввёл свои данные в требуемом формате, можно позаботиться и о пароле.

Напишите функцию password_validation, которая принимает один позиционный параметр — пароль, и следующие именованные параметры:

min_length — минимальная длина пароля, по умолчанию 8;
possible_chars — строка символов, которые могут быть в пароле, по умолчанию латинские буквы и цифры;
at_least_one — функция возвращающая логическое значение, по умолчанию str.isdigit.
Если переданный позиционный параметр не является строкой, вызовите исключение TypeError.

А так же реализуйте собственные исключения:

MinLengthError — вызывается, если пароль меньше заданной длины;
PossibleCharError — вызывается, если в пароле используется недопустимый символ;
NeedCharError — вызывается, если в пароле не найдено ни одного обязательного символа.
Проверка условий должна происходить в порядке указанном в задании.

Так как, хороший разработчик никогда не хранит пароли в открытом виде, функция, в случае успешного завершения, возвращает хеш пароля. Для этого воспользуйтесь функцией sha256 из пакета hashlib и верните его шестнадцатеричное представление.

Примечание
В решении не должно быть вызовов требуемых функций.

Пример 1
Ввод
print(password_validation("Hello12345"))
Вывод
67698a29126e52a6921ca061082783ede0e9085c45163c3658a2b0a82c8f95a1
Пример 2
Ввод
print(password_validation(
    "$uNri$e_777",
    min_length=6,
    at_least_one=lambda char: char in "!@#$%^&*()_"
))
Вывод
Вызвано исключение PossibleCharError
"""
