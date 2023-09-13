# Перетирание значений при создании нескольких инстансов декарируемого класса. В примере, при создании нескольдких экземпляров для класса С.

class Decorator:
    def __init__(self, C):
        self.C = C
    
    def __call__(self, *args): # Потенциальная проблема. Существует всего один инстанс Decorator для одного класса С. И здесь перетираем.
        self.wrapped = self.C(*args)
        return self
    
    def __getarttr__(self, attrname):
        return getattr(self.wrapped, attrname)
    
@Decorator
class C:    # C = Decorator(C)
    pass

x = C()
y = C() # Здесь вызывается снова __call__ который создаст новый инстанс класса С и перетрёт значение для "x" ->  self.wrapped = self.C(*args)

# Для этого либо нужно использовать декоратор метод либо пример из decorator_for_class.py