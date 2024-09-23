#-*-coding:utf-8-*-

class Base(object):
	def __init__(self):
		print('Base.__init__')

class A(Base):
    '''
        Это как???
    '''
    def spam(self):
        print('A.spam')
        super().spam()
        # super(A, self).spam() # Вся фишка здесь. Почему вызывается "B.spam"? Он спускается вниз, дойдя до Base???
        # Если здесь закомментировать, то вызова "B.spam" не произойдёт.
        
        
    __localValA = "---'It is privateClassValue that defined in A class.'---"
    publicValA = "---'It is publicClassValue that defined in A class.'---"
    
    @classmethod
    def cl(cls, a):
        print(cls.__localValA + ' ' + a)
        # Это работает, но закомментировал т.к. есть вероятность зациклить, если в обоих методах расскоментировать
        # cls.st(" ::: Call staticMethod form ClassMethod.")
        
    @staticmethod
    def st(a):
        print(A.__localValA + " " + a)
        # Это работает, но закомментировал, т.к. вызов еще и в classmethod - дабы избежать зацикливания.
        # A.cl(" ::: Call classMethod form StaticMethod. Note, that doesnt pass the class to the classMethod")
        
class B(Base):    
    def spam(self):
        print('B.spam')

class C(A, B):
    """
        В обоих случаях используется эта реализация а не из А класса.
    """
    @classmethod
    def cl(cls, a):
        print(cls.publicValA + " ::: It is overloaded class function. And Arg = " + a)
        
    @staticmethod
    def st(a): # Говорят, что classmethod нужен для доступа к переменным класса. Однако и у статик метода такая возможность есть.
        print(A.publicValA + " ::: It is overloaded static function. And Arg = " + a )

print(C.mro())
y = C()
y.spam() #

#Вывод
#[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>]
#Base.__init__
#A.spam
#B.spam

print(type(y) == C)
print(C.__class__) 
print(y.__class__)
print(id(C))

# Вызво класс и статик методов.
y.cl("::: 'Argumeth for classMethod' ")
y.st("::: 'Argumeth for staticMethod' ")

C.cl("Просто класс метод")
C.st("Просто статик метод")


