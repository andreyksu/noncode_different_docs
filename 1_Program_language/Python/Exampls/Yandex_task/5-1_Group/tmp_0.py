class A:
	aa = "String_1"

	def a(self):
		print("a() A.a = ", A.aa)
		print("a() self.a = ", self.aa)

	def b(self, a):
		self.aa = a

	def c(self):
		print("c() self.a = ", self.aa)
		print("c A.a = ", A.aa)

inst = A()
inst.a()
inst.b("String_2")
inst.c()


xxx = 23

if xxx is not None:
    print("xxx is not None 1")
if not xxx is None:
    print("not xxx is None 2")
if not (xxx is None):
    print("not (xxx is None) 3")
if xxx is None:
    print("xxx is None")
    
    
print (not None)
