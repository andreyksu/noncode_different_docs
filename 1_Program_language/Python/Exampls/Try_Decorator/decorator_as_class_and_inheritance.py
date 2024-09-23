# Рассмотреть кейс с дочерним классом для декоратора.
# Декоратор класа.

from typing import Any

def wrap(cls):
    class wrapper: # Но методы операций вида __x__ нужно будет ручками в этом классе делать. Вопрос, а получится ли сделать явный вызов?
        def __init__(self, *args, **kwargs):
            self.tragetObj = cls(*args, **kwargs)

        def __call__(self, *args, **kwargs):
            print("It is __call__ of wrapper class")
            return cls.__call__(self.tragetObj, *args, **kwargs) # Вызов __call__ для декорированного класса.

        def __getattr__(self, __name: str) -> Any: # В этом классе атрибуты не будут найдены. И будет вызван этот метод. А в этом методе происходит переадресация обёрнутому объекту.
            print('Will be called the method with name = %s' % __name)
            tmp = __name
            return getattr(self.tragetObj, tmp)

    return wrapper

@wrap
class A:
    def __init__(self, newVar):
        self.newVar = newVar

    def __call__(self, *args, **kwargs):
        print("In is call of the A class self.newVar = %s" % self.newVar)
        return "Wass Called A__call__"

    def method(self, param):
        self.param = param
        print("It is method of A class and param = %s" % param)

class B(A):
    pass


a = A("___A_Value_for_variable___")
a.method('__A_INVOKE__')

print("---------------------------------------------------")

b = B("___B_Value_for_variable___") # Тоже замечательно работает с таким декоратором wrapper
b.method('__B_INVOKE__')
print(b())

#------------------------Попробовать с классом-декоратором-дескриптором------------------------