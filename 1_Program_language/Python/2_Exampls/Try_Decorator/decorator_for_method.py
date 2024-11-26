# Декоратор для обычного метода но не для метода класса (для метода класса будет потерян self см. decorator_for_method_of_class_doesnt_work_lost_self.py)

class tracer:# То что представленно от Лутца. Плюсом добавил __new__ исключительно для вывода отладочной информации.
    def __new__(cls, *args, **kargs):
        print ("__new__  cls = %s" % (cls))
        return object.__new__(cls)

    def __init__(self, func):             # On @ decoration: save original func
        self.calls = 0
        self.func = func
        print('__init__    Self =  %s, Hash = %s' % (self, self.__hash__)) # Вывод, для контроля что это различные объекты. Что при каждом привязывании создаётся новый объект

    def __call__(self, *args):            # On later calls: run original func
        self.calls += 1
        print('Coutn invoce __call__ = %s for Function =  %s' % (self.calls, self.func.__name__))
        print('__call__    Self =  %s, Hash = %s' % (self, self.__hash__))
        self.func(*args)

    @staticmethod
    def a(cls, a):
        pass

class tracer1: # Пример сделал свой - альтернативный вариант. Пример с передачей параметров. Првоерял, тоже создаются разные объекты.
    def __new__(cls, *args, **kargs):
        print ("__new__  cls = %s" % (cls))
        return object.__new__(cls)

    def __init__(self, aParam):
        self.instance = 0
        self.param = aParam
        print("aParam = %s" % aParam)

    def __call__(self, aFunc):
        self.instance += 1
        self.func = aFunc
        print('Create new Wrapper instance_wrapper_count = %s to Function = %s' % (self.instance, self.func.__name__))
        print('Self =  %s, Hash = %s' % (self, self.__hash__))
        #return self.func
        return self.someMethod #Возвращаем метод. При этом, что интересно привязка к объекту присутствует. Т.е. метод остается связанным (по терминалогии Лутц)
    
    @staticmethod
    def a(cls, a):
        pass
    
    def someMethod(self, *agrs):
        print("This is the someMethod self = %s self.instance = %s and self.param = %s" % (self, self.instance, self.param))        
        resultOfMethod = self.func(*agrs)
        return resultOfMethod
        

@tracer
def spam_1(a, b, c):           # spam = tracer(spam)
    print("Hello from 'spam_1'")
    print(a + b + c)         # Wraps spam in a decorator object

@tracer
def spam_2():
    print("Hello from 'spam_2'")

print("--------------------------------------------------------")

@tracer1("First")
def spam_3(a, b, c):           # spam = tracer(spam)
    print("Hello from 'spam_3'")
    print(a + b + c)         # Wraps spam in a decorator object

@tracer1("Second")
def spam_4(FirstParam):
    print("Hello from 'spam_4' FirstParam = %s" % FirstParam)


print("--------------------------------------------------------")
spam_3(1, 2, 3)
spam_3(4, 5, 6)

spam_4(1)
spam_4(2)