class A:
    def __init__(self, a):
        self.a = a

    def __call__(self, *args, **kwargs): # Всё что передано входит в перечнь args
        print("str(args) = %s" % str(args))
        print("__call__ of A class")

    def method(self):
        print("self.a = %s" % self.a)


first = A("First")
second = A("Second")

first(second, "A", "B")

A.method(second)
A.method(first)