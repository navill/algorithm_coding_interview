"""
BST의 다음 노드 탐색 알고리즘
[2,3,4,5,6,7]
        4
    2       6
  1  (3)  5  7
target이 2일 경우 다음 노드는 3
= target의 오른쪽 하위 노드(rchild)가 있을 경우 -> rchild
target이 3일 경우 다음 노드는 4
target의 오른쪽 하위 노드가 없을 경우 -> parent
target이 7일 경우 다음 노드는 None

"""
from chapter_4.create_tree import create_tree


class Node:

    def __init__(self, node=None):
        self.node = node
        self.parent = None
        self.lchild = None
        self.rchild = None


def inorder_succ(node):
    if node is None:
        return None

    if node.rchild:
        # rchild에서 가장 왼쪽 노드를 찾는다.
        return left_most_child(node.rchild)
    else:
        n = node  # (2)
        p = node.parent  # (4)
        # p.lchild(2) == n(2) -> break while
        #   target node와 tartget.parent.lchild 같음 => target의 다음 노드는 target의 부모 노드가 된다.
        while p is None and p.lchild != n:
            n = p
            p = p.parent
        return p  # return 4


def left_most_child(node):
    if node is None:
        return None
    while node.lchild:
        node = node.lchild
    return node


li_bst = [1, 2, 4, 5, 6, 7]  # BST
node_bst = create_tree(li_bst, 0, 5)

a = Node(4)
a.parent = None
b = Node(2)
b.parent = a
a.lchild = b
c = Node(6)
c.parent = a
a.rchild = c
d = Node(1)
d.parent = b
b.lchild = d
e = Node(5)
e.parent = c
c.lchild = e
f = Node(7)
f.parent = c
c.rchild = e

"""
         4(a)
    2(b)       6(c)
  1(d)       5(e)  7(f)
"""

print(inorder_succ(b).node)
