# См. decorator_for_method_of_class_doesnt_work_lost_self.py - здесь описаны мысли как можно было бы сделать.
# Но не получается т.к. в @Decorator(self) не удаётся получить доступ к self

# См. рабочий вариант decorator_for_method_of_class_by_descriptor.py - через декоратор-дексриптор.
class Decorator:
    def __new__ (cls, *args, **kargs):
        print("__new__ Created new Instance of Decorator_class")
        return super().__new__(cls)

    def __init__(self, aInstance):
        print("__init__ Created new Instance of Decorator_class")
        self.instance = aInstance

    def __call__(self, aFunc):
        self.func = aFunc
        return self.targetMethod

    def targetMethod(self, *args):
        print("This is target method of Decorator class. Self = %s and TargetInstance = " % (self, self.instance))
        self.func(self.instance, *args)


class C:
    def __new__ (cls, *args, **kargs):        
        print("__new__ Created new Instance of C_class")
        return super().__new__(cls)

    def __init__(self):
        print("__init__ Created new Instance of C_class")

    @Decorator(self)    # Хотелось бы как-то так. Но здесь и на этом этапе о self ничего не известно. # И второй момент, декоратор будет вызван на этапе создания класса а не создания экземпляра от этого класса. Соответственно self еще не создан.
                        # Таков порядок работы создания класса. Выполняются все инструкции внутри class. Происходит формирование пространства имён класса, а так как декоратор это перепревязка имение, декоратор будет вызван на этапе создания класса и self еще не существует.
    def method(self, x, y):
        print("This is the Method in C class. Param x = %s, y = %s" % (x, y))

x = C()
x.method(x, 1, 2)

y = C()
y.method(y, 1, 2)

