"""
가장 작은 값이 가장 위로 오도록 스택을 정렬하는 알고리즘

s1  s2          s1  s2          s1  s2          s1  s2
------          ------          ------          ------
    12              12          8               8
5   8   ->          8   ->      12      ->      12  5
10  3           10  3           10  3           10  3
7   1           7   1           7   1           7   1
tmp = None      tmp = 5         tmp = 5         tmp = None

1. while not s1.isempty()가 True일 때까지 반복
2.      기존 스택(s1)에 있는 값을 pop() -> tmp에 저장
3.      while not s2.isempty() and s2.peek() > tmp 비교(tmp가 s2.peek보다 작을 때 까지 반복)
                s1.push(s2.pop())
4.      순환문이 끝나면 s2.push(tmp)
5. s1=빈 stack, s2=내림차순으로 정렬된 stack이 된다.
6. s1.push(s2.pop()) -> s1에 오름차순으로 정렬=> s1.top에 가장 작은 값이 위치한다.
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

    def isempty(self):
        if self.size():
            return False
        else:
            return True


def stack_sort(s1):
    s2 = Stack()
    while not s1.isempty():
        tmp = s1.pop()
        while not s2.isempty() and s2.peek() > tmp:
            s1.push(s2.pop())
        s2.push(tmp)
    while not s2.isempty():
        s1.push(s2.pop())


s = Stack()
s.push(7)
s.push(5)
s.push(2)
s.push(3)
s.push(6)
stack_sort(s)
print(s.li)
