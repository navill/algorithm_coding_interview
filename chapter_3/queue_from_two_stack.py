"""
두 개의 stack을 이용해 queue 구현
"""


class Stack:
    def __init__(self):
        self.li = list()

    def push(self, data):
        self.li.append(data)

    def pop(self):
        if self.li:
            return self.li.pop()

    def peek(self):
        if self.li:
            return self.li[-1]

    def size(self):
        return len(self.li)

    def empty(self):
        if self.size():
            return False
        else:
            return True


class MyQueue:
    def __init__(self, *args, **kwargs):
        self.stack_new = Stack()
        self.stack_old = Stack()

    def size(self):
        return self.stack_new.size() + self.stack_old.size()

    def add(self, value):
        self.stack_new.push(value)

    def shift_stack(self):
        if self.stack_old.empty():
            while not self.stack_new.empty():
                self.stack_old.push(self.stack_new.pop())

    def peek(self):
        self.shift_stack()
        return self.stack_old.peek()

    def remove(self):
        self.shift_stack()
        return self.stack_old.pop()


stack = MyQueue()
stack.add(1)
stack.add(2)
stack.add(3)
print(stack.remove())  # 1
print(stack.remove())  # 2
stack.add(1)
print(stack.remove())  # 3
print(stack.remove())  # 1
