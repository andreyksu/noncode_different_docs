# Это продолжение decorator_for_method_of_class_doesnt_work_lost_self.py - как можно избежать потерю self при декорировании метода ---> декоратором-классом.
# На помощь приходит декоратор-класс-дескриптор. Который через __get__ возвращает объект хранящий две ссылки (ссылку экземпляра для декорируемого метода и ссылку на экземпляр декоратор).
class tracer(object):
    def __init__(self, func):
        self.calls = 0 
        self.func = func

    def __call__(self, *args, **kwargs): # self.tracer(self.instance, ...) вот здесь переменная self.instance войдет в перечень переменных *args
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        print('self = %s /n/t str(args) = %s' % (self, str(args))) # То что self.instance вошло в перечень *args видно здесь при выводе.
        return self.func(*args, **kwargs)
    
    def __get__(self, instance, class_of_instance): # У метода два этапа: Первое - поиск и извлечение имени. Второе - выполнение. По этой причине - первое - get. Второе - call
        return wrapper(self, instance)

class wrapper:
    def __init__(self, tracer, instance):
        self.tracer = tracer
        self.instance = instance

    def __call__(self, *args, **kwargs):
        print("tracer = %s name = %s " % (self.tracer, self.tracer.__class__))
        print("instance = %s name = %s " % (self.instance, self.instance.__class__))
        return self.tracer(self.instance, *args, **kwargs)  # tracer - это объект, переданный при создании wrapper. Соответственно, здесь вызов __call__.
                                                            # В __call__ передаётся объект для дальнейшей передачи в метод (дабы исключить потерю self) - см. decorator_for_method_of_class_doesnt_work_lost_self.py

@tracer
def spam(a, b, c):
    pass

class Person:
    @tracer # giveRAise = tracer(giveRAise)
    def giveRAise(self, percent):
        print("Person class inside giveRAise self = %s " % self)
        pass

pers = Person()
pers.giveRAise("percent")


#--------------------------- А здесь сохраняется привязка к экземпляру. А все потому, что привязка идёт после создания экземпляра.
class A:
    def __init__(self, a):
        self.a = a
    def meth(self):
        print(self.a)

class B:
    def __init__(self, func):
        self.func = func

    def doMeth(self, *args):
        self.func(*args)

a1 = A(1)
a2 = A(2)
m = a1.meth

b = B(m)

b.doMeth()
