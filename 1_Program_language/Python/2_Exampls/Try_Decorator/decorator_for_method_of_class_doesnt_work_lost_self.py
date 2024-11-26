# Так не работает т.к. для обёрнутого метода теряется self (вернее не передаётся). Согласно Лутцу - это только для декоратора-класса. Для декоратора-метода все нормально - self не теряется.
# См. decorator_for_method_of_class_doesnt_work_lost_self_thinking.py - это просто размышление. Но не рабочее.
# См. decorator_for_method_of_class_by_descriptor.py - рабочий вариант. Как это решается через декаратор-дескриптор (там создаётся отдельный объект, который и хранит self для обёрнутого метода и сслыку на декоратор - этот объект возвращается методом __get__)
class Decorator:
    def __new__ (cls, *args, **kargs):
        print("__new__ Created new Instance of Decorator_class")
        return super().__new__(cls)

    def __init__(self, aFunc):
        print("__init__ Created new Instance of Decorator_class")
        self.func = aFunc

    def __call__(self, *args):
        self.func(*args)

class C:
    def __new__ (cls, *args, **kargs):        
        print("__new__ Created new Instance of C_class")
        return super().__new__(cls)

    def __init__(self):
        print("__init__ Created new Instance of C_class")

    @Decorator # Тождественно method = Decorator(method) - и при вызове method - будует передан self для Decorator, а self для С - не будет передан.
    def method(self, x, y): # В исключении будет [TypeError: method() missing 1 required positional argument: 'y'] - т.е. на лицо потеря self и смещение параметров влево.
        print("x = %s, y = %s" % (x, y)) 
        # Лутц 5изд стр. 525.
        # Формально интерпретатор создаёт объект связанного метода, содержащий экземпляр цеоевого класса. только когда метод представляет собой простую функцию, на не вызваемый экземпляр еще одного класса.

x = C()
x.method(1, 2)  # Здесь по сути идёт вызов переменной класса С и на этом шаге передаётся self экземпляра класса С. Но дальше уже внутри класса С при вызове обёртки (сама обёртка) в метод method разумеется self класса С не передаётся.
                # Т.е. если сделать так чтоб в сам декоратор был передан экземпляр класса С. Т.е. в виде @Decorator(self) - тогда возможно и заработает.
#x.method(x, 1, 2) # По-хорошему нужно запускать так (т.е. добавлять объект для которого вызываем данный метод)

#Правильный вариант
def decorator(F):
    def wrapper(*args):
        print("In wrapper method")
        F(*args)
    return wrapper

@decorator # func = decorator(func)
def func(x, y):
    print(x + y)

func(1, 2) # По факту вызывается wrapper(1, 2)

class C:
    @decorator # method = decorator(method) - создаётся связанная переменная.
    def method(self, x, y):
        print(x * y)

X = C()
X.method(3, 4) # По факту вызывается wrapper(X, 6, 7)