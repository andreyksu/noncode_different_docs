# Здесь важно, что при каждом обращении к методу а() будет создаваться новый класс-объект.
# Метакласс добавлен лишь для демонстрации того, что создаётся ноывй класс-объект.

class MyMeta(type):
    count_of_class = 0
    
    def __new__(meta, className, supers, argsDict): # Для обычного класса meta - это cls
        print("It is __new__ object Class meta = %s" % meta)
        return type.__new__(meta, className, supers, argsDict)
    
    def __init__(classObj, className, supers, argsDict): # Для обычного класса classObj  - это self
        MyMeta.countt_of_class = MyMeta.count_of_class + 1 # Не поняетно почему здесь без имени класса не работает.
        print("It is __init__ object Class  = %s" % MyMeta.count_of_class)
        

def a():
    class MyClass(metaclass=MyMeta):
        def __init__(self):
            self.clss = 'Clss'
            
        def printt(self):
            print(self.clss)
            
    return MyClass

theMyClass = a()    # Создаётся класс-объект
print(id(theMyClass)) # Свой id
theMyClass1 = a()   # Создаётся еще один класс-объект
print(id(theMyClass1)) # Свой id, отличный от предыдущего.
instanceOfMyClass = theMyClass() # Создание экземпляра от класса, что вернули из метода.
instanceOfMyClass.printt()
print(type(theMyClass))
print(type(instanceOfMyClass))