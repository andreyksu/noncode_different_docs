#-*- coding:utf-8 -*-
from b_pack.a_pack import a_mod as modA # Здесь добавляется тек. модуль т.к. запускается c_mod а путь строится именно от него (по сути classPath)

def printAllMethodOfModA():
    print("ModBB---" * 8)
    print(id(modA))
    print(f'!!! Прямой доступ к modA.strrAA = {modA.strrAA}')
    modA.printOwnAttr()
    modA.printStrrAA()    
    print("ModBB===" * 8)

    