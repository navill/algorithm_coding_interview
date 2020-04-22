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


"""
push할 때 스택 사이즈를 초과할 경우 새로운 스택 생성 -> stack list에 추가 
stack size = 4
stack list = [
[1,2,3,4]  # stack1
]
stack list push = 5
stack list = [
[1,2,3,4],  # stack1
[5]         # stack2
]
...
stack list = [
[1,2,3,4],  # stack1
[5,6,7,8],  # stack2
[9,10,11,12],  # stack3
[13,14,15,16],  # stack4
]

stack list pop => 16
stack list pop => 15
stack list pop => 14

 
"""