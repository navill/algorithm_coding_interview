"""
이진 트리에서 두 개의 노드에 대한 공통 부모를 찾는 알고리즘
- 부모 노드에 대한 링크가 없을 경우
- 부모 노드에 대한 링크가 있을 경우

        20
    10      30
  5    15
3  7(p)  17(q)

"""
from chapter_4.create_tree import create_tree


# 부모노드에 대한 링크가 있을 경우
class Node:
    def __init__(self, node=None):
        self.node = node
        self.parent = None
        self.lchild = None
        self.rchild = None


def common_ancestor(root, p, q):
    if not covers(root, p) or not covers(root, q):
        return None
    elif covers(p, q):
        return p
    elif covers(q, p):
        return q

    sibling = getsibling(p)  # 7의 형제: 3
    parent = p.parent  # 부모: 5
    while not covers(sibling, q):
        sibling = getsibling(parent)  # 부모의 형제 -> getsibling(5): 15
        parent = parent.parent  # 부모의 부모: 10
        # => 부모 10은 자식 17을 덥을 수 있음
    return parent  # 부모 10 반환


def covers(root, p):
    if root is None:
        return False
    if root == p:
        return True
    return covers(root.lchild, p) or covers(root.rchild, p)


def getsibling(node):
    if node is None or node.parent is None:
        return None
    parent = node.parent
    return parent.rchild if parent.lchild == node else parent.lchild


li = [3, 5, 7, 10, 15, 17, 20, 30]
node = create_tree(li, 0, 7)  # BST
print(node.node)
node1 = Node(20)
node2 = Node(10)
node2.parent = node1
node3 = Node(30)
node3.parent = node1
node1.lchild = node2
node1.rchild = node3
node4 = Node(5)
node4.parent = node2
node5 = Node(15)
node5.parent = node2
node2.lchild = node4
node2.rchild = node5
node6 = Node(3)
node6.parent = node4
node7 = Node(7)
node7.parent = node4
node4.lchild = node6
node4.rchild = node7
node8 = Node(17)
node8.parent = node5
node5.rchild = node8

common_ancestor(node1, node7, node8)  #


# 부모에 대한 링크가 없을 경우


class Node:
    def __init__(self, node):
        self.node = node
        self.lchild = None
        self.rchild = None


def common_ancestor2(root, p, q):
    # 두 값(p,q)가 루트에 연결되어 있는지 검사
    if not covers2(root, q) or not covers(root, q):
        return False
    return ancestor_helper(root, p, q)


def ancestor_helper(root, p, q):
    # TC: O(2N) = O(N)
    is_left_p = covers2(root.lchild, p)  # 왼쪽 N
    is_left_q = covers2(root.lchild, q)  # 오른쪽 N

    # 두 노드가 모두 루트의 왼쪽 자식에 포함되는지 확인
    # => 서로 다를 경우 root가 공통 노드가 된다.
    if is_left_p != is_left_q:
        return root
    child_side = root.lchild if is_left_p else root.rchild
    return ancestor_helper(child_side, p, q)


def covers2(root, p):
    if root is None:
        return False
    if root == p:
        return True
    return covers2(root.lchild, p) or covers2(root.rchild, p)


print(ancestor_helper(node1, node7, node8).node)
