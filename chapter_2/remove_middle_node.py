"""
처음과 끝이 아닌 노드 하나를 삭제하는 알고리즘
접근은 삭제할 노드만 가능
a->b->c->d->e
삭제 노드: c
결과: a->b->d->e
"""


# linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def delete_node(node):
    if node is None or node.next is None:
        return None
    next_node = node.next
    node.data = next_node.data
    node.next = next_node.next


node1 = Node('a')
node2 = Node('b')
node1.next = node2
node3 = Node('c')
node2.next = node3
node4 = Node('d')
node3.next = node4
node5 = Node('e')
node4.next = node5

delete_node(node3)
print(node1.data)
