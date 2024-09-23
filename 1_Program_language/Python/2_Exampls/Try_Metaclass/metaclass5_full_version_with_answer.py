# Classes can catch calls too (but built-ins look in metas, not supers!)

class SuperMeta(type):
    def __call__(meta, classname, supers, classdict): # Вызов этого метода происходит когда создаётся объект класс Spam
# Когда создаётся класс-объет Spam в конце его определения происходит вызов его метакласса Spam_Class = SubMeta(....). Т.к. SubMeta это объкт, то вызов SubMeta(...) означает вызов __call__(...).
# А учитывая правило c() <=> type(с).__call__(с) мы имеем для вызов type(SubMeta) - вернёт SuperMeta и вызовет его __call__(...)
        print('In SuperMeta.call: ', meta, classname, supers, classdict, sep='\n\t\t')
        newInstance = type.__call__(meta, classname, supers, classdict) # Видимо, сигнатура __call__ для создания объекта класса отличается от сигнатуры __call___ для создания экземпляра класса.
        print('!!! In SuperMeta.call: newInstance ', newInstance, sep='\n\t\t') # Внимание на вывод. Выводится после __init__ и __new__. Что 
        return newInstance

    def __init__(Class, classname, supers, classdict):
        print('In SuperMeta init:', Class, classname, supers, classdict, sep='\n\t\t')
        print('\t\t\t init class object:', list(Class.__dict__.keys()))

print('making metaclass')
class SubMeta(type, metaclass=SuperMeta):
# Этот метод вызывается когда создаётся экземпляр от Spam. Почему? А потому, что создание экземпляра происходит так Spam(...) а что такое Spam? А Spam это объект. Значит вызов Spam(...) эхвивалентен вызову __call__
# А учитывая правило c() <=> type(с).__call__(с) мы имеем для вызова type(Spam)  - вернёт SubMeta и вызовет его __call__(...)
    def __call__(cls, *args, **kargs): # Сигнатура __call__  для создания экземпляра класса отлаичается от сигнатуры __call__ для создания объект-класса.
        print('In SubMeta.call: ', cls, str(args), str(kargs), sep='\n\t\t')
        newInstance = type.__call__(cls, *args, **kargs)
        print('In SubMeta.call: newInstance ', newInstance, sep='\n\t\t')
        return newInstance
    
    def __new__(meta, classname, supers, classdict):
        print('In SubMeta.new: ', meta, classname, supers, classdict, sep='\n\t\t')
        # newInstance = super().__new__(meta, classname, supers, classdict)
        newInstance = type.__new__(meta, classname, supers, classdict)
        print('In SubMeta.new: newInstance ', newInstance, sep='\n\t\t')
        return newInstance

    def __init__(Class, classname, supers, classdict):
        print('In SubMeta init:', Class, classname, supers, classdict, sep='\n\t\t')
        print('\t\t\t init class object:', list(Class.__dict__.keys()))

class Eggs:
    pass

print('making class Spam')
class Spam(Eggs, metaclass=SubMeta):        # Invoke SubMeta, via SuperMeta.__call__ 
    def __new__(cls, *args, **kargs):
        print('In Spam.new: ', cls, str(args), str(kargs), sep='\n\t\t')
        # newInstance = super().__new__(cls)
        newInstance = Eggs.__new__(cls)
        print('In Spam.new: newInstance ', newInstance, sep='\n\t\t')
        return newInstance

    data = 1
    def meth(self, arg):
        return self.data + arg

print('making class SubSpam')
class SubSpam(Spam):
    pass

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))
