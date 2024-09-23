#-*- coding:utf-8 -*-

# Проверяется импорт модулей и изменение значений атрибутов для импоритрованных модулей.

# Внимание, участвуют три модуля a_mod, b_mod, c_mod.
# Центральный c_mod - модуль. a_mod и b_mod импортируется.


from b_pack.a_pack import a_mod as modA
from b_pack import b_mod as modBB  

print(id(modA))         # См. что выводит здесь и то что выводится в модулe bb - это одно ID

modA.strrA='Modified value in other module' # Изменили переменную в импортированном модуле.
modA.strrAA='Was added in b_mod'  # Добавили новую переменную в ИМПОРТИРОВАННЫЙ модуль! Ошибку не выдало. 
modA.listtA.append(4)   # Изменили переменную в импортированном модуле.

modA.printInttA()
modA.printStrrA()
modA.printStrrAA() # Просим модуль "a" - вывести переменную которую добавили здесь. Т.е. в "а" - этой переменной не было
modA.printListtA()

modBB.printAllMethodOfModA()