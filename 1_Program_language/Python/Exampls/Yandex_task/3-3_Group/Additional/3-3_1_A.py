readed_a = input()
readed_b = input()

elements_of_a = readed_a.split("=")
elements_of_b = readed_b.split("=")

a = elements_of_a[-1].strip()
b = elements_of_b[-1].strip()

a = int(a)
b = int(b)

x = [y**2 for y in range(a, b + 1)]

print(x)
