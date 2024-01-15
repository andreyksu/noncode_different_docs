def func():
    x = int("Hello, world!")


def func():
    x = "2" + 2


try:
    func()
except ValueError as e:
    print("ValueError")
except TypeError as e:
    print("TypeError")
except SystemError as e:
    print("SystemError")
else:
    print("No Exceptions")


"""
Обработка ошибок
Вашему решению будет предоставлена функция func, которая не имеет параметров и результата. Однако во время её исполнения может произойти одна из ошибок: ValueError, TypeError или SystemError.

Вызовите её, обработайте ошибку и выведите её название. Если ошибка не произойдёт, выведите сообщение "No Exceptions".

Пример 1
Ввод
    def func():
        x = int('Hello, world!')
Вывод
    ValueError
Пример 2
Ввод
    def func():
        x = '2' + 2
Вывод
    TypeError
"""