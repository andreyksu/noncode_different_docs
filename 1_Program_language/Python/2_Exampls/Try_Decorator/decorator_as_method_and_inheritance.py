# Рассмотреть кейс с дочерним классом для декоратора.
# Декоратор как метод

def decorA(func):
    def wrapperA(*args, **kwargs):
        print("It is form DecorA")
        return func(*args, **kwargs)
    return wrapperA

def decorB(func):
    def wrapperB(*args, **kwargs):
        print("It is form DecorB")
        return func(*args, **kwargs)
    return wrapperB

class A:
    @decorA
    def methdod(self, a):
        print("A___class and param = %s" % a)
        return a
    
class B(A):
    @decorB # Переопределение работает как для метода с 
    def methdod(self, a):
        print("B___class and param = %s" % a)
        return a

a = A()
print(a.methdod("A_to_method"))

print("---------------------------------------------------")

b = B()
print(b.methdod("B_to_method"))