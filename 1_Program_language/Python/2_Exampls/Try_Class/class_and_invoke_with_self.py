class A:
    def __init__(self, a):
        self.a = a

    def __call__(self, *args, **kwargs): # Всё что передано входит в перечнь args
        for i in args:
            print("i = %s" % i)
        print("self.a = %s" % str(self.a))
        print("__call__ of A class")

    def method(self):
        print("self.a = %s" % self.a)


first = A("First")
second = A("Second")

first(second, "A", "B") # second будет в *args а не в self

A.method(first)
A.method(second)
