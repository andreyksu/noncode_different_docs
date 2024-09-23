import os

user = os.getlogin()

print(user)

# Внешний метод, что будет привязан вне класса.
def outer_method(self):
    # Добавляем новое поле к объектам
    self.new_field_from_outer_method = "self.new_field_from_outer_method"
    # Обращаемся к существующим полям.
    print("From Outer methdo instanceVal = " + self.inst_field)
    
# Внешний метод, что будет привязан внутри класса.
def outer_method_1(self):
    print(self.__class__)

class A:
    static_field = 'static_field_value'
    
    # Привязка внешнего метода к полю.
    outer_methodd = outer_method_1
    
    # self.f = 'f' # Так нельзя. 
    # Однако если сделать так, то скажет, что NameError: name 'self' is not defined
    # Что говорит, о том, что на этом этапе еще не объявлено self. Все верно, ведь instance еще не создан.
    
    def __init__(self, param):
        self.inst_field = param
        # А так не работает. Т.к. ВИДИМО метод принадлежит классу а не объекту. 
        # Во всяком случае ругается, что метод не получает self.
        # self.outer_methodd = outer_method_1

    def inner_method(self):
        print("Work with static method form simple method = " + A.static_field)
        
    def edit_field(self, newparam):
        A.static_field = newparam
        self.inst_field = newparam
        
    def printer(self):
        print("-" * 80)
        print("Static field = " + A.static_field)
        print("Instant field = " + self.inst_field)
        print("+" * 80)

# Привязка к полю класса - внешний метод.
A.some = outer_method        
                
class B(A):
    def __init__(self, param):
        super().__init__(param)
        # A.__init__(self, param) # А можно и так.
        # super(A, self).__init___(param) # А можно и так.

B.static_field = "Param" # Создали одноименную переменную для класса B.
print(B.static_field) # Для класса B новая переменная
print(A.static_field) # Для класса А свноя локальная переменная.

b_inst = B("b_inst")
b_inst_1 = B("b_inst_1")

# Добавили поле в класс после объявления инстенсов.
B.static_field_1 = "Param1" # Статик поле.
b_inst.new_inst_val = 'new_isnt_val' # Поле для инстенса.

b_inst.printer() # Внимание, что здесь будет выведено. Ведь указано A.static_field

b_inst.edit_field("New Val")
b_inst.printer()
b_inst_1.printer()

b_inst.some() # Тоже смотрим сюда. Это вызов внешнего привязанного класса.

# А вот можно сделать так. Взять и добавить поле и поработать с ним.
print(b_inst.new_field_from_outer_method)

print(b_inst_1.static_field_1)  # Выведет Param1
print(b_inst.static_field_1)    # Выведет Param1
print(b_inst.new_inst_val)      # Выведет new_isnt_val
#print(b_inst_1.new_inst_val)   # Нет такого поля в этом экземпляре. Ведь добавлено в b_inst
b_inst_1.outer_methodd()