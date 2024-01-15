def func(a, b, c):
    return "".join(map(str, (a, b, c)))


def func(a):
    print(str(a))
    return str(a)


try:

    class MyObject:
        def __str__(self):
            raise Exception("")

        def __repr__(self):
            raise Exception("")

    func(MyObject())
except Exception:
    print("Ура! Ошибка!")


"""
Ломать — не строить 2
Вашему решению будет предоставлена функция func, которая на этот раз принимает неограниченное число позиционных параметров и производит с ними некую операцию приведения типа.

Предложите вызов функции, который гарантированно породит ошибку внутри функции.

Примечание
Если ошибка произойдёт внутри функции, то она будет перехвачена и обработана.
Если же она произойдет в вашем коде, то программа будет завершена с ошибкой.

Пример 1
Ввод
    def func(a, b, c):
        return ''.join(map(str, (a, b, c)))
Вывод
    Ура! Ошибка!
    Пример 2
Ввод
    def func(a, b):
        return set(a) ^ set(b)
Вывод
    Ура! Ошибка!
"""
