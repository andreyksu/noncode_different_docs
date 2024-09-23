# Снова вопрос к метатипу, а именно к super(). См. комментарии ниже.
# И вопросы соответственно к вызову type.__init__(...) и super.__init__(...) и object.__init__(...)


class meta(type):
    def __new__(meta_Class, name_targetClass, parentClassList, dictOfAttr):
        print("It is __new__ of class meta")
        return type.__new__(meta_Class, name_targetClass, parentClassList, dictOfAttr)

    def __init__(target_Class, name_targetClass, parentClassList, dictOfAttr):
        print("It is __init__ of class meta START")
        print(
            super().__name__
        )  # <<<<< Почему вывод ::: А ??? Как может быть у meta супертип это А ???
        print(super().__bases__)
        print(target_Class)
        print("It is __init__ of class meta END")
        # object.__init__(name_targetClass, parentClassList, dictOfAttr) # <<<<< ???
        type.__init__(
            target_Class, name_targetClass, parentClassList, dictOfAttr
        )  # <<<<< ???


class A(metaclass=meta):
    def __init__(self, param):
        self.param = param

    def __call__(self, a, b):
        print(
            "It is __call__ in A class a = %s , b = %s, param = %s "
            % (a, b, self.param)
        )


a = A("First")
a(1, 2)
type(a).__call__(a, 1, 2)

b = A("Second")
A.__call__(b, 3, 4)
