class Node:
    def __init__(self, data=None):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, d):
        self.__data = d

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        self.__next = n


class Stack:
    def __init__(self):
        self.top = None

    def push(self, d):
        node = Node(d)
        node.next = self.top  # 초기 self.top은 None
        # .next는 이전의 노드를 가리킴 (ex: 1,2,3,4에서 node(4).next는 node(3)을 가리킨다.)
        self.top = node

    def pop(self):
        if self.empty():
            return None
        pop_node = self.top
        self.top = self.top.next
        return pop_node.data

    def empty(self):
        if self.top is None:
            return True
        else:
            return False

    def peek(self):
        if self.empty():
            return None
        return self.top.data


st = Stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
print(st.peek())
print(st.pop())
print(st.peek())
print(st.pop())
print(st.pop())
print(st.pop())
print(st.peek())
print(st.pop())
print(st.peek())
