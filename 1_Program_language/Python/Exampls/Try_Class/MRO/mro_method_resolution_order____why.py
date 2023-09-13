#-*-coding:utf-8-*-

class Base(object):
	def __init__(self):
		print('Base.__init__')

class A(Base):
    def spam(self):
        print('A.spam')
        super(A, self).spam() # Вся фишка здесь. Почему вызывается "B.spam". Если здесь закомментировать, то вызова "B.spam" не произойдёт.

class B(Base):
    def spam(self):
        print('B.spam')

class C(A, B):
    pass

print(C.mro())
y = C()
y.spam()

#Вывод
#[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>]
#Base.__init__
#A.spam
#B.spam