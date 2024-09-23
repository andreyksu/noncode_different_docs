"""
Пример MRO для конструкторов.
"""

class Animal(object):
	def __init__(self):
		print('Animal.__init__')

class Wild(Animal):
    def __init__(self):
        # super().__init__() # Это работает только внутри метода. Внутри @staticmethdo или @classmethod так работать не будет.
        # super(Wild, self).__init__()
        Animal.__init__(self) # Внутри(интерпретатора) все превращается в такой вид.
        print('Wild.__init__')
    
    def say(self):
        print('Wild.say')

class Mammal(Animal):
    def say(self):        
        print('Mammal.say')

class Tiger(Mammal, Wild):
    pass

# Здесь Mammal не имеет своего конструтора и будет вызван конструктор Animal.__init__
mammal = Mammal()
mammal.say()

# Здесь Tiger не имеет своего конструтора и будет вызван конструктор Wild.__init__ см. MRO
tiger = Tiger()
tiger.say() # Wild.__init__
print(Tiger.mro()) # [<class '__main__.Tiger'>, <class '__main__.Mammal'>, <class '__main__.Wild'>, <class '__main__.Animal'>, <class 'object'>]