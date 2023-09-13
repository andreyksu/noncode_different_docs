def decorator(target_cls): # Создаётся новый класс, который и возвращается данным методом. А новый класс-обёртка внутри себя содержит инстнас класса, который обернулии и перенаправляет ему свои запросы.
    class Wrapper:
        def __new__(cls, *args, **kargs): # Добавил исключительено для отладки.
            print("In Wrapper_class   cls.__name__ = %s" % cls.__name__)
            return super().__new__(cls)

        def __init__(self, *args):
            self.wrapped = target_cls(*args)

        # Нужно помнить, что данные методы в Pу3 не используются для поиска встроенных операций (т.е. методов вида __x__. Пример __add__ итд т.к. )
        def __getattr__(self, name): # Всё остальное, что не будет найденно в классе Wrapper - будет искаться в С.
            return getattr(self.wrapped, name)
        
        def __getattribute__(self, name):
            print("It from method __getattribute__ name = %s" % name)
            return object.__getattribute__(self, name)

    return Wrapper

@decorator
class C:
    def __new__(cls, *args, **kargs):
        print("In C_class   cls.__name__ = %s" % cls.__name__)
        return super().__new__(cls)

    def __init__(self, x, y):
        self.attr = 'spam'

    def __add__(self, athor): # Если убрать над классом С декорирование, т.е. закомментировать. То данный метод будет работать. А с декоратором данный метод не работает.
        return "Parammmmmm"

x = C(6, 7)
print(x.attr)

#x1 = C(6, 7) # Не работает при наличии декоратора. Т.к. __getattr__ не перехватывает обращение к таким методам. Если закомментировать декорирование, то сложение сработает.
#print(x+x1)