#-*- coding:utf-8 -*-

class ClassA:
	data = 'spam'

	# В новых классах, метод уже не используется для поиска неявных вызовов. Допустим для "+" не будет искаться __add__.
	def __getattr__(self, name):	# Метод используется если целевое поле не было найдено не в инстансе и не в классе. Тоже использует self.
		print("__getattr__ name = %s" % name)
		return getattr(self.data, name) # Глобальный метод. Не привязан к классу. Используется для вызова атрибута у целевого объекта.

	def __getitem__(self, index):
		print("__getitem__  index = %s" % index)
		return self.data[index:index+1] #При возврате используем копию/срез

X = ClassA()
res = X[2] 	# Вот в Python3 если бы метода __getitem__ не был бы объявлен, то метод __getattr__ НЕ был бы вызван для поиска __getitem__. Т.к. в классах нового типа данные методы не используются для неявного вызова методов вида __x__
			# А в python2 __getitem__ использовался бы для поиска __getitem__.
res_1 = type(X).__getitem__(X, 2) # А это прямое общращение к __getitem__ и оно нормально работает в Python3

# Тоже явный вызов, но почему-то в книге не приведён пример. В чем может быть подвох?
res_2 = X.__getitem__(3)

# Пример не в тему, но показывает, что в первом случае поиск для неявного вызова + -> __add__ не осуществляется. А во втором случае, при явном вызове __add__ поиск осуществляется.
z1 = ClassA()
z2 = ClassA()
# z1 + z2 # Поиска  __add__ нет.
# z1.__add__(z2) # Поиск __add__ есть.