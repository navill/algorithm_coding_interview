from chapter_4.create_tree import create_bst
from chapter_4.tree_traversal import *

"""
이진 트리가 균형 잡혀있는지 확인하는 함수
- 왼쪽 트리와 오른쪽 트리의 높이 차가 최대 1
        3
    1       5
      2   4   6

get_height(root)  -- 3(root)
=> left부터 재귀 진행
get_height(lchild) -- 1(left.root)
    get_height(lchild) -- None
    |    return - 1             # a = -1  
    get_height(rchild) -- 2
    |    get_height(lchild) -- None
    |    |    return - 1        # b = -1
    |    get_height(rchild) -- None
    |    |    return - 1        # c = -1
    max(b, c) + 1 = rchild가 0 반환  # d = 0
max(a, d) + 1 = lchild가 1 반환
left 종료

get_height(lchild) -- 5(right.root)
    get_height(lchild) -- 4
    |    get_height(lchild) -- None
    |    |    return -1
    |    get_height(rchild) -- None
    |    |    return -1
    max(-1, -1) + 1 = lchild가 0반환  # A = 0
    get_height(rchild) -- 6
    |    get_height(lchild) -- None
    |    |    return -1
    |    get_height(rchild) -- None
    |    |    return -1
    max(-1, -1) + 1 = rchild가 0반환  # B = 0
max(A, B) + 1 = lchild가 1반환                
right 종료
"""


def get_height(root):
    if root is None:
        return -1
    return max(get_height(root.lchild), get_height(root.rchild)) + 1


def is_balanced(root):
    if root is None:
        return True
    diff = abs(get_height(root.lchild) - get_height(root.rchild))
    if diff > 1:
        return False
    else:
        return is_balanced(root.lchild) and is_balanced(root.rchild)


li = [1, 2, 3, 4, 5, 6]
# bst
bst = create_bst(li, 0, 5)
print(is_balanced(bst))
# in_order_traversal(bst)
# pre_order_traversal(bst)
# skewed tree
skewed_tree = Node(1)
b = Node(2)
skewed_tree.lchild = b
c = Node(3)
b.lchild = c
d = Node(4)
c.lchild = d
# print(is_balanced(skewed_tree))
