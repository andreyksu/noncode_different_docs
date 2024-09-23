# Пример добавления классу метода через декоратор
def newMethod(self, param):
    self.param = param
    print("newMethod ==="  + str(param))

def decor(cls):
    cls.meth = newMethod
    return cls    


@decor
class F:
    def __new__(cls, *args, **kargs):
        instance =  object.__new__(cls)
        return instance

    def __init__(self, aA, aB):
        self.a = aA
        self.b = aB
        pass

    def printt(self):
        print(self.a + self.b)

f0 = F("First ", "Second")
f1 = F("Third ", "Fourth")

f0.meth(1)
f1.meth(2)
print(f0.param)