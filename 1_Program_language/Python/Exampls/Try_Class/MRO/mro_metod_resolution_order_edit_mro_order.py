#-*-coding:utf-8-*-

class Base(object):
	def __init__(self):
		print('Base.__init__')

class A(Base):	
	def __init__(self):
		print('A.__init__')
		super().__init__()

class B(Base):	
	def __init__(self):
		print('B.__init__')
		super().__init__()

class C(A, B):
	def __init__(self):
		print('C.__init__')
		super().__init__() #Так будет вызван согласно mro. Тождественный вывод будет и для super(C, self).__init__() при этом передётся текущий класс, а не родительский.
		#B.__init__(self) #Так можно поменять порядок, задав свой.

x = C()

print(C.__mro__)
print(C.mro())

#Вывод для super().__init__():
#C.__init__
#A.__init__
#B.__init__
#Base.__init__
#(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>)
#[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>]

#Вывод для B.__init__(self):
#C.__init__
#B.__init__
#Base.__init__
#(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>)
#[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>]