# Пример простого дескриптора. Дескрипторы работают с полями класса, а не полями экземпляра. По этой причине нужно быть онимательнее при использовании состояния дескриптора.
class Descriptor:
    def __init__(self, param):
        self.param = param
        
    "Descriptor for Name"
    def __get__(self, instance, owner_class):        
        print("__get__ method of Descriptor")
        print("self.param = %s" % self.param)
        print("instance = %s, owner_class = %s" % (instance, owner_class))
        return instance._name # Возвращается поле экземпляра класса Person (делается для независимой работы с экземплярами)
        # Т.е. мы не можем сетить значение полю декриптора, т.к. дескриптор один на все экземпляры класса Person. Приходится работать через поля экземпляра.
    
    def __set__(self, instance, value):
        print("__set__ method of Descriptor")
        instance._name = value  # Устанавливается поле экземпляра класса Person (делается для независимой работы с экземплярами)

    #def __set__(self, instance, value):
    #    raise AttributeError("can`t set value to the field")

    def __delete__(self, instance):
        print("__delete__ method of Descriptor")
        del instance._name

class Person:
    def __init__(self, name):
        self._name = name
    
    # По сути объявление дескриптора по отношению к полю класса похоже не объявление декоратора. Ведь декоратор повторно привязывает имени метода/класса своё представление.
    name = Descriptor("In is the name value") # Дескриптор работает только с переменной класса, а не с переменной экземпляра. По этой причине (для поддержки работы с экземплярами), в дескрипторе работа ведется с экземпляром класса Person.


bob = Person("Bob")
print(bob.name)