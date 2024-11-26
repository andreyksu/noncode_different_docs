#-*- coding:utf-8 -*-
#--------------------------------------------------------
#Что выведет:
i = [1, 2, 3]
def func2(arg = i):
	length = len(arg)
	arg[length:] = [4, 5]
	print ("arg =====", arg)

func2()
i = [100, 200, 300]
func2()
# ---------------- Инициализация один раз.
i = [1, 2, 3]
def func2(arg):
	arg = i # Если так
	length = len(arg)
	arg[length:] = [4, 5]
	print ("arg =====", arg)

func2()
i = [100, 200, 300]
func2()

#--------------------------------------------------------
#Что выведет:
# a_arg ===== [100, 101]
# innerFunc()  [5, 4] 6
# innerFunc()  [5, 4] 4

a = [1, 2]
d = 3


def func(a):
    print("a_arg =====", a)
    a = [3, 4]
    d = 4

    def innerFunc1():
        a[0] = 5
        d = 6 # Здесь убрать
        print("innerFunc() ", a, d)
        d = 6 # И здесь убрать. Что будет. А если сдесь добавить добавить?

    def innerFunc2():
        print("innerFunc() ", a, d)

    return (innerFunc1, innerFunc2)


f1, f2 = func([100, 101])
f1()
f2()

#--------------------------
# Что выведет? Почему?
# 101
# 101

def func(d):
    d = 1    
    def change_d(dd):
        nonlocal d
        d = dd

    kk = lambda first, second=d: print(first+second)

    return (change_d, kk)

ch, kk = func(500)
kk(100)
ch(20)
kk(100)