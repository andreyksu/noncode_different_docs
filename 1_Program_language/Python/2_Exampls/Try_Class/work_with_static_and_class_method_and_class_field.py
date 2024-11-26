class AA:
    attr = "AA class"

    def __init__(self):
        self.first = "AA_class __init__"
        print("It is the 'AA' class '__init__' and first = ", self.first)

    def printerAA(self):        
        print("It is the 'AA' class 'printerAA' and first = ", self.first)

    @staticmethod
    def printAttrAA():
        print("printAttrAA() AA.attr = %s" % AA.attr)

    @classmethod
    def printerClsAA(cls):
        print("printerClsAA() cls = %s" % cls) # Т.е. при наследовании, сюда будет передаваться дочерний класс (разуммется, этот комментарий относится к чистому виду, т.е. без переоределения в дочернем классе)
        print("printerClsAA() cls.attr = %s" % cls.attr) # С переопределением всё понятно, там само собой будет class BB. Но то что здесь cls == BB - это удивительно.

class BB(AA):
    attr = "BB class"

    def __init__(self):
        AA.__init__(self)
        self.first = "BB_class __init__"
        print("It is the 'BB' class '__init__' and first = ", self.first)

    def printerBB(self):
        self.first = "BB_class printerBB"
        print("It is the 'BB' class 'printerBB' and first = ", self.first)
        AA.printerAA(self)

    @staticmethod
    def printAttrBB():
        print("printAttrBB() AA.attr = %s" % AA.attr)
        print("printAttrBB() BB.attr = %s" % BB.attr) # К чему привязано, такое значение и выведет.

    # @staticmethod # Интересно! Переопределение статических методов работает. Т.е. будет использован этот метод.
    # def printAttrAA():
    #    print("Override printAttrBB() AA.attr = %s" % AA.attr) 
        
    @classmethod
    def printerClsBB(cls):
        print("printerClsBB() cls = %s" % cls)
        print("printerClsBB() cls.attr = %s" % cls.attr)

    # @classmethod # Интересно! Переопределение методов класса работает. Т.е. будет использован этот метод.
    # def printerClsAA(cls):
    #    print("Override printerClsAA() cls = %s" % cls)
    #    print("Override printerClsAA() AA.attr = %s" % cls.attr)
        
bb = BB()
bb.printerBB()

bb.printAttrAA()
bb.printAttrBB() # К чему привязано, такое значение и выведет.

bb.printerClsAA() # Хаааа, а тут будет класс BB (это речь идёт без перегрузки) ---> printerClsAA() cls.attr = BB class
bb.printerClsBB()