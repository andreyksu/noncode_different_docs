#-*-coding:utf-8-*-

def numbers_range(n):
    print("In function")
    for i in range(n):
        print("In For")
        yield i
a = numbers_range(4)
print(type(a))
print(dir(a))
print(type(numbers_range))
for b in a:
    print(b)
    
