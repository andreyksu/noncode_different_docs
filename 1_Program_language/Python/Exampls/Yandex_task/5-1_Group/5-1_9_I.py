class Queue:
    def __init__(self):
        self.listt = list()
        self.firstPosition = 0
        self.lastPosition = 0

    def push(self, item):
        self.lastPosition += 1
        self.listt.append(item)

    def pop(self):
        if self.firstPosition == self.lastPosition:
            return None
        tmp_item = self.listt[self.firstPosition]
        self.firstPosition += 1
        return tmp_item

    def is_empty(self):
        if self.firstPosition == self.lastPosition:
            return True
        else:
            return False

    def get_pos(self):
        return f"firstPos = {self.firstPosition}, lastPos = {self.lastPosition}"


queue = Queue()
for item in range(10):
    queue.push(item)
print(queue.get_pos())
while not queue.is_empty():
    print(queue.pop(), end=" ")
print(queue.get_pos())

print()
print("-" * 100)
queue = Queue()
for item in ("Hello,", "world!"):
    queue.push(item)
print(queue.get_pos())
while not queue.is_empty():
    print(queue.pop())


print(queue.get_pos())
