class People:
    def __init__(self, aName):
        self.name = aName
        
    def printName(self):
        print(self.name + " " + "This is the People class\n")
        
    @staticmethod
    def staticMethod():
        print("ThisIsStaticMethod in People\n")
        
class Emploer(People):
    def __init__(self, aName):
        People.__init__(self, aName)
        
    def someMethod(nameName):
        print(nameName)

        
people = People("Oleg")
people.printName()
people.staticMethod()

emploer = Emploer("Masha")
emploer.printName()
emploer.staticMethod()
emploer.someMethod("dddd")