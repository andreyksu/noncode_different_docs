# Атрибуты функции

def func(param : str, param2: (1, 10) = 3) -> None: # Это просто аннотации. Допустим param2 - ограничение ни к чему не обвязвает, просто подсказка. Аналогично и по типу.
    if(param.__class__ == str):
        print("Да первый параметр соответствует классу String (==) И объекты param = %s и str = %s" % (param.__class__, str))
        print("id(param.__class__) = %s и id(str) = %s" % (id(param.__class__), id(str)))
    if(param.__class__ is str):
        print("Да первый параметр соответствует классу String (is)")
    someAttr = "someAttr"
    print("param = %s;     param2 = %s " % (param, param2))
    print(f'func.newAttr = {func.newAttr}') # Вот как можно обращаться к атрибуту, что был добавлен к методу.
    #print(newAttr) # Так нельзя. Исключение (NameError: name 'newAttr' is not defined)
	
func.newAttr = "NewAttr"

func('param')
func('param', 50)
#print(func.someAttr) # Так нельзя. Исключение (AttributeError: 'function' object has no attribute 'someAttr')
print(func.newAttr)


print("-" * 40)
print(func.__code__)
print("-" * 40)
print(func.__class__)
print("-" * 40)
print(func.__name__)
print("-" * 40)
print(dir(func.__code__))
print("-" * 40)
print(dir(func))
print("-" * 40)
print(func.__annotations__)
