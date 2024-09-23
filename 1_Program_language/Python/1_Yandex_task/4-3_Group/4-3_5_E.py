def result_accumulator(func):
    listt = list()

    def decor(*args, method="accumulate"):
        result = func(*args)
        if method == "accumulate":
            listt.append(result)
            return None
        elif method == "drop":
            listt.append(result)
            newList = listt[:] # Не нравится эта часть. Постоянное создание нового списка.
            listt.clear()
            return newList

    return decor


@result_accumulator
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5, method="accumulate"))
print(a_plus_b(7, 9))
print(a_plus_b(-3, 5, method="drop"))
print(a_plus_b(1, -7))
print(a_plus_b(10, 35, method="drop"))


@result_accumulator
def get_letters(text: str) -> str:
    return "".join(sorted(set(filter(str.isalpha, text.lower()))))


print(get_letters("Hello, world!"))
print(get_letters("Декораторы это круто =)"))
print(get_letters("Ехали медведи на велосипеде", method="drop"))

"""
Накопление результата
В некоторых случаях полезно накапливать результат, а затем получать его единым списком.

Реализуйте декоратор result_accumulator, который модернизирует функцию с неопределенным количеством позиционных параметров следующим образом:

Добавляет именованный параметр method со значением по умолчанию accumulate;
При вызове функции с параметром method равным accumulate, результат сохраняется в очередь (для каждой функции в собственную), а функция ничего не возвращает;
При вызове функции с параметром method равным drop, возвращается все накопленные результаты, а очередь сбрасывается.
Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Пример 1
Ввод
@result_accumulator
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5, method="accumulate"))
print(a_plus_b(7, 9))
print(a_plus_b(-3, 5, method="drop"))
print(a_plus_b(1, -7))
print(a_plus_b(10, 35, method="drop"))
Вывод
None
None
[8, 16, 2]
None
[-6, 45]
Пример 2
Ввод
@result_accumulator
def get_letters(text: str) -> str:
    return ''.join(sorted(set(filter(str.isalpha, text.lower()))))


print(get_letters('Hello, world!'))
print(get_letters('Декораторы это круто =)'))
print(get_letters('Ехали медведи на велосипеде', method='drop'))
Вывод
None
None
['dehlorw', 'адекортуыэ', 'авдеилмнопсх']
"""