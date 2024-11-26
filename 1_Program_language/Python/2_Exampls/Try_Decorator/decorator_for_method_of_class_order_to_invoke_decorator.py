# Пример, отражающий порядок обращения к декоратору метода класса
# Рабочий пример декорирования метода класса (где не теряется self для декорированного метода класса)
# Работает и для обычных методов, методов вне класса.
def dec(func):
    print("It is dec")
    def wrap(*args):
        print("It is wrap")
        func(*args) # !!! Здесь обычно возвращают результат функции. А не просто вызывают. См. ниже.
    return wrap

class A:
    def __new__(cls, *args, **kargs):
        print("__new__")        
        return super().__new__(cls)
    
    def __init__(self) -> None:
        print (self.__dict__)
        print (self.__dir__)
        pass

    @dec # Декторатор будет вызван еще на этапе создания класса. А не создания экземпляра. Это соответствует порядку создания класса и его пространства имён.
    def method(self):
        print("Method in class A")
    
#a = A() # Даже с закомментированной этой строчкой будет выполнен код декоратора.
        
# Вот более полный пример, с именованными переменными/параметрами. Но вопрос, а вот как это всё работате во многопточке???
def decor(func):
    calls = 0
    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        return func(*args, **kwargs)
    return wrapper

@decor
def spam(a, b, c):
    print(a + b + c)

spam(1, 2, 3)
spam(a=4, b=5, c=6)

# Интересный аналог, где к объекту функции присоединяется атрибут.

def decor1(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0 # Это будет выполнено, до выполнения функции wrapper. Т.е. таким образом мы добавляем атрибут и присваиваем значение.
    return wrapper

@decor1
def spam1(a, b, c):
    print(a + b + c)

spam1(1, 2, 3)
spam1(a=4, b=5, c=6)