#-*- coding:utf-8 -*-

inttA = 1
strrA = 'It is assign in a_mod'
listtA = [1, 2, 3]

def printInttA():
    print(f"inttA = {inttA} ")
    
def printStrrA():
    print(f"strrA = {strrA} ")
    
def printListtA():
    print(f"listtA = {listtA} ")
    
def printOwnAttr():
    printInttA()
    printStrrA()
    printListtA()
    
def printStrrAA(): # Выводит переменную, что присоединили к модулю в др. модуле. См. модуль b
    print(f"modA.strrAA = {strrAA} ")
    # Т.е. изначально этой переменной модуль не содержит. А добавляетс в модуле b.
    # Разумеется пример синтетический, но для наглядности подходит.