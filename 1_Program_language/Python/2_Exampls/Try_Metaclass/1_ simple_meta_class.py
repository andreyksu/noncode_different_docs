def methodd(self, arg):
    print("Hello From method added in meta")

class Meta(type):
    the_static = 0
    
    def __new__(meta_cls, className, supers, classdict): # В обычном классе meta_cls - это cls. cls - это объект класса, а здесь видимо объенк мета-класса. В данном случае объект класса Meta.
        print("Hello from new of the __new__ meta: className = " + className)
        print("Hello from new of the __new__ meta: meta_cls = " + str(meta_cls))
        return type.__new__(meta_cls, className, supers, classdict) # className - string, className - tuple, classdict - словарь переменных и их значений.

    # Т.е. здесь идёт наполнение объекта класса. Др. словами инициализация иобъекта класса.
    def __init__(obj_cls, className, supers, classdict): # В обычном классе obj_cls - это self. self инстенс, кторый создали, а здесь obj_cls тоже объект но объект класса.
        Meta.the_static = Meta.the_static + 1 
        obj_cls.field_added_in_meta = "Hello from meta"
        obj_cls.target_method = methodd
        print("Hello from new of the __init__ meta: className = " + className)
        print("Hello from new of the __init__ meta: obj_cls = " + str(obj_cls))


# Метакласс вызывается в конце, что приведено в качестве доказательства в логах ниже.
# Получается куда, к какому объекту привязывается 'classField' -  если объект создается внизу класса методом __new__ метакласса Meta
class TargetClass(metaclass=Meta):
    print("In targetClass --- First")
    classField = 'class_field'
    def mehtod(self):
        pass
    print("In targetClass --- Second")

# Выдаст
# In targetClass --- First
# In targetClass --- Second
######### А дальше пошли вызовы метакласса.
# Hello from new of the __new__ meta: className = TargetClass
# Hello from new of the __new__ meta: meta_cls = <class '__main__.Meta'>
# Hello from new of the __init__ meta: className = TargetClass
# Hello from new of the __init__ meta: obj_cls = <class '__main__.TargetClass'> # Это уже объект-класса.


print(TargetClass.field_added_in_meta)
# Hello from meta
tc = TargetClass()
tc.target_method("Some Args")