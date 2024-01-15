class Stack:
    def __init__(self):
        self.currentPos = -1
        self.listt = list()

    def push(self, item):
        self.currentPos += 1
        self.listt.insert(self.currentPos, item)

    def is_empty(self):
        if self.currentPos < 0:
            return True
        return False

    def pop(self):
        if self.currentPos < 0:
            return None
        tmp = self.listt[self.currentPos]
        self.currentPos -= 1
        return tmp


stack = Stack()
for item in ("Hello,", "world!"):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop())


stack1 = Stack()

print(stack1.is_empty())
print(stack1.push(1))
print(stack1.is_empty())
print(stack1.pop())
print(stack1.is_empty())
print(stack1.pop())
print(stack1.is_empty())


"""
Стек
Ещё одной полезной коллекцией является стек реализующий принцип «Последний пришёл – первый ушёл». Его часто представляют как стопку карт или магазин пистолета, где приходящие элементы закрывают выход уже находящимся в коллекции.

Реализуйте класс Stack, который не имеет параметров инициализации, но поддерживает методы:

push(item) — добавить элемент в конец стека;
pop() — «вытащить» первый элемент из стека;
is_empty() — проверяет стек на пустоту.
Примечание
Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Пример 1
Ввод
    stack = Stack()
    for item in range(10):
        stack.push(item)
    while not stack.is_empty():
        print(stack.pop(), end=" ")
Вывод
    9 8 7 6 5 4 3 2 1 0     
Пример 2
Ввод
    stack = Stack()
    for item in ("Hello,", "world!"):
        stack.push(item)
    while not stack.is_empty():
        print(stack.pop())
Вывод
    world!
    Hello,
"""