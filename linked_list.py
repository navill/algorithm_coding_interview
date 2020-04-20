class Node:
    def __init__(self, data=None):
        self.__next = None
        self.__data = data

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


# linked list
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = None

li = list()
li.append(a)
li.append(b)
li.append(c)
li.append(d)
li.append(e)

print(a.data)
for i in range(len(li) - 1):
    print(li[i].next.data)
