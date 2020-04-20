# class Node:
#     def __init__(self, data=None):
#         self.__next = None
#         self.__data = data
#
#     @property
#     def data(self):
#         return self.__data
#
#     @data.setter
#     def data(self, d):
#         self.__data = d
#
#     @property
#     def next(self):
#         return self.__next
#
#     @next.setter
#     def next(self, n):
#         self.__next = n
#
#
# class Q:
#     def __init__(self, *args, **kwargs):
#         self.front = None
#         self.rear = None
#
#     def empty(self):
#         if not self.front:
#             return True
#         return False
#
#     def enqueue(self, d):
#         node = Node(d)
#         if self.empty():
#             self.front = node
#             self.rear = node
#         else:
#             self.rear.next = node
#             self.rear = node
#
#     def dequeue(self):
#         if self.empty():
#             return None
#         deq_value = self.front
#         self.front = self.front.next
#         return deq_value
