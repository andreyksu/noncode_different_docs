# Classes can catch calls too (but built-ins look in metas, not supers!)

class SuperMeta(type):
    def __call__(meta, classname, supers, classdict): #Вот он ломающий голову метод. Почему он не вызывается когда создаётся объект-класс SubMeta??? 
	# У Лутц_а говорится так: Метод вызывается встроенной операцией (т.е. вызывается неявно) от сюда все нюансы.
	# Если посмотреть файл metaclass5_hmm.py то, там раскрывается что значит неявно. Вызов SomeClass(....) - является неявным.
	# Суперкласс пропускается для встроенных имён(видимо, здесь вся соль этого примера). А вот для явного извеления, не пропускается см. metaclass5_hmm.py и полагается на обычное наследование имён.
	# Но не понятно, а где здесь наследование????
        print('In SuperMeta.call: ', meta, classname, supers, classdict, sep='\n\t\t')
        newInstance = type.__call__(meta, classname, supers, classdict)
        print('!!! In SuperMeta.call: newInstance ', newInstance, sep='\n\t\t')
        return newInstance
# См. metainstance.py и особенности __call__ - в там файле он вызывается только при создании экземпляра от класса, но не вызывается при создании самого класса. И при этом он и отличается по сигнатуре.

    def __init__(Class, classname, supers, classdict):
        print('In SuperMeta init:', Class, classname, supers, classdict, sep='\n\t\t')
        print('\t\t\t init class object:', list(Class.__dict__.keys()))

print('making metaclass')
class SubMeta(type, metaclass=SuperMeta):
    def __call__(cls, *args, **kargs):
        print('In SubMeta.call: ', cls, str(args), str(kargs), sep='\n\t\t')
        newInstance = type.__call__(cls, *args, **kargs)
        print('In SubMeta.call: newInstance ', newInstance, sep='\n\t\t')
        return newInstance
    
    def __new__(meta, classname, supers, classdict):
        print('In SubMeta.new: ', meta, classname, supers, classdict, sep='\n\t\t')
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
    data = 1
    def meth(self, arg):
        return self.data + arg

print('making class SubSpam')
class SubSpam(Spam):
    pass

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))
