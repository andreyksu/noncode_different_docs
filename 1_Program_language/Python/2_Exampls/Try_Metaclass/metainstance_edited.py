# File metainstance.py

class MetaOne(type):
# Это то, как предсталвенно в интернетах.
# Этот код работывает когда происходит создание экземпляра от класса Sub. А не когда создается сам класс Sub.
# Это верно с учетом привила для функций вида __х__ ::: c() <=> type(с).__call__(с)
# Т.е. с учётом правила  c() <=> type(с).__call__(с). Т.е. при создании экземпляра Sub в виде Sub() будет вызван type(Sub).__call__(Sub) - а это MetaOne
    def __call__(cls, *args, **kargs): # У Лутц __call__ для метакласса имеет другую сигнатуру (набор параметров). Но это верно, ведь у Лутца там метакласс для метакласса.
        print('In MetaOne.call cks === "%s" args === "%s"' % (cls, str(args)))
        someInst = type.__call__(cls, *args, **kargs)
        return someInst # В метаклассе важно иметь return для __call__  с обращением к родителю. Иначе не создастся экземпляр класса Sub. И тут видимо вызов к object???? Не очень понимаю с сигнатурами. Обе к type


# Здесь этот __call__ не будет вызван никогда.

#    def __call__(meta, classname, supers, classdict):
#        print('In MetaOne.call:', classname)
#        return type.__call__(meta, classname, supers, classdict)

    def __new__(meta, classname, supers, classdict):        # Redefine type method
        print('In MetaOne.new:', classname)
        return type.__new__(meta, classname, supers, classdict) # Важно иметь return для __new__ с обращением к родителю
    
    def toast(self):
       return 'toast'

class Super(metaclass=MetaOne):        # Metaclass inherited by subs too
    def spam(self):                    # MetaOne run twice for two classes
        return 'spam'

class Sub(Super):                      # Superclass: inheritance versus instance
    def eggs(self):                    # Classes inherit from superclasses
        return 'eggs'                  # But not from metclasses
    
    def __call__(self, *args):
        print("Sub.__call__")

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("a = %s, b = %s" % (a, b))

    def __call__(self, *args):
        print("Sub.__call__  where::: args = %s" % str(args))

print("__________Start Create Instance__________".upper())
x = Sub(1, 2)   #Вызывает __call__(meta, *args, **kargs) из метакласса. Но почему? Ведь __call__ из метакласса должен вызываться при создании самого класса, а не его экземпляров.
x("ddd", "bbb") #Вызывает __call__ из Sub - что верно.
