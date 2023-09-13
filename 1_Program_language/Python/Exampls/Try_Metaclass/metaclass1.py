class MetaOne(type):
# Касается комментария ниже. Пока не дописал особенности, что выяснил но моменто в следующем x() = type(x).__call__(x) см. metaclass5_full_version_with_answer.py

# Исходно у Лутц_а файл без этого метода. Но вроде все сделано по аналогии с metaclass5.py но при этом, здесь будет ошибка при создании X = Spam()
#    def __call__(meta, classname, supers, classdict): 
#        print("__call__ in MetaOne")
#        return type.__call__(meta, classname, supers, classdict)
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', meta, classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

class Eggs:
    pass

print('making class')
class Spam(Eggs, metaclass=MetaOne):      # Inherits from Eggs, instance of MetaOne
    data = 1                              # Class data attribute
    def meth(self, arg):                  # Class method attribute
        return self.data + arg

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))
