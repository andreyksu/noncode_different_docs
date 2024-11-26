def metaFunc(className, supers, classdict):
    print("It is body of Meta function ")
    return type(className, supers, classdict) # Это вызов __call__ у класса type

class TargetClass(metaclass=metaFunc):
    print("In targetClass --- First")
    classField = 'class_field'
    def mehtod(self):
        pass
    print("In targetClass --- Second")

# Выдаст
# In targetClass --- First
# In targetClass --- Second
# It is body of Meta function