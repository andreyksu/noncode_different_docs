#-*- coding:utf-8 -*-
from b_pack.a_pack import a_mod as modA # Здесь добавляется тек. модуль т.к. запускается c_mod а путь строится именно от него (по сути classPath)

print(f'b_mod dir() = {dir()}') # Без аргумента выводит информацию для тек. окружения.

print("ModBB---" * 8)
modA.printOwnAttr()
modA.printStrrAA()
print("ModBB===" * 8)
   