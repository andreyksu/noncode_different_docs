#-*-encoding:utf-8-*-
class Person:
	string3 = "string3" #Переменная уровня класса (по сути public static в терменологии Java)
	string4 = "string4"


	print("This will be dine once = {} + {}".format(string3, string4))

	def disp(self, string):
		self.string1 = "string1"	#Новая переменная уровня объекта
		string2 = "string2"			#Новая локальная переменная уровня метода disp(...)
		print("disp string = {}".format(string))
		print("disp self.string1 = {}".format(self.string1))
		print("New field of Method disp string2 = {}".format(string2))
		print("disp self.string3 = {}".format(self.string3))
		#print("disp string3 = {}".format(string3)) #NameError: global name 'string3' is not defined
		print("disp self.string4 = {}".format(self.string4))

	def disp1(self, string):
		self.string1 = "string1_1"	#Всё та же переменная уровня объекта что объявлена в методе disp(...)
		string2 = "string2_1"		#Новая локальная переменная уровня метода disp1(...)
		string3 = "string3_1"		#Новая локальная переменная уровня метода disp1(...)
		self.string3 = "string3_1_1"#А здесь что? Создается переменная уровня ОБЪЕКТА, что перекрывает переменную уровня КЛАССА?
		print("disp1 string = {}".format(string))
		print("disp1 self.string1 = {}".format(self.string1))
		print("New field of Method  disp1 string2 = {}".format(string2))
		print("disp1 self.string3 = {}".format(self.string3))
		print("New field of Method withOut SELF disp1 string3 = {}".format(string3))
		print("disp1 self.string4 = {}".format(self.string4))

p = Person()
p1 = Person()
print("--------------------------")
p.disp("Hllo")
print("--------------------------")
p.disp1("Hllo_1")
print("--------------------------")
print("p.string1 = {}".format(p.string1))
#print("p1.string1 = {}".format(p1.string1))
print("---------")
print("p.string3 = {}".format(p.string3))
print("p1.string3 = {}".format(p1.string3))
p2 = Person()
print("p2.string3 = {}".format(p2.string3))
print("Person.string3 = {}".format(Person.string3))
print("-------------Person.string3 = dddddd-------------")
Person.string3 = "dddddd" #Не влияет на значение p.string3 т.к. в методе disp1(...) создана переменная уровня объекта и она перекрывает перменнную уровня класса?
print("Person.string3 = {}".format(Person.string3)) ### Вот здесь ведет себя как статик.
print("p.string3 = {}".format(p.string3))  ### А здесь что? Создано поле не класса а объекта в методе disp1()????
print("p1.string3 = {}".format(p1.string3)) ### Вот здесь ведет себя как статик.
print("p2.string3 = {}".format(p2.string3)) ### Вот здесь ведет себя как статик.