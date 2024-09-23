# Пример создания класса с методом __new__ - он всегда вызывает метод у object - т.к. __new__ в object реализован на C/C++ и именно он создаёт объект.

class A():
    def __new__(cls, *param, **param1):
        print("That is the __new__ = " + str(cls))
        return object.__new__(cls)
        # return super().__new__(*param)
    
    def __init__(self, param):
        self.param = param
    
    def printt(self):
        print(self.param)
        
# Такое создение
a = A("Pr") # Выдаст "That is the __new__ = <class '__main__.A'>"
        
# Эквивалентно тому что сверху, но в ручном режиме.
instanceA = A.__new__(A, "Pr")
if isinstance (instanceA, A):
    A.__init__(instanceA, "Pr") # Эквивалентно instanceA.__init__("Pr") 
instanceA.printt()


