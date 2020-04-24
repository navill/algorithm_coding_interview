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
    |    return max(b, c) + 1 = rchild(2)가 0 반환  # d = 0
    return max(a, d) + 1 = lchild(None)가 1 반환
left 종료

get_height(lchild) -- 5(right.root)
    get_height(lchild) -- 4
    |    get_height(lchild) -- None
    |    |    return -1
    |    get_height(rchild) -- None
    |    |    return -1
    |    return max(-1, -1) + 1 = lchild(4)가 0반환  # A = 0
    get_height(rchild) -- 6
    |    get_height(lchild) -- None
    |    |    return -1
    |    get_height(rchild) -- None
    |    |    return -1
    |    return max(-1, -1) + 1 = rchild(6)가 0반환  # B = 0
    return max(A, B) + 1 = lchild(5)가 1반환                
right 종료  

TC: O(NlogN)
"""


def get_height(root):  # 높이 측정 + 균형 검사
    if root is None:
        return -1
    return max(get_height(root.lchild), get_height(root.rchild)) + 1


def is_balanced(root):
    if root is None:
        return True
    diff = abs(get_height(root.lchild) - get_height(root.rchild))
    if diff > 1:
        return False  # 반환 대상 Boolean
    else:
        return is_balanced(root.lchild) and is_balanced(root.rchild)  # 반환 대상 Boolean


"""
위 방식은 같은 노드에 대해 get_height()이 호출되기 때문에 낭비가 생긴다 -> get_height 호출을 줄여야 한다.
"""

false_number = 99999999999  #


def check_height(root):  # 높이 측정 + 균형 검사
    if root is None:
        return -1
    l = check_height(root.lchild)
    r = check_height(root.rchild)
    diff = l - r
    if abs(diff) > 1:
        return false_number  # 반환 대상 Integer - 불균형 상태
    else:
        # 노드의 깊이를 반환 - 균형된 상태
        return max(check_height(root.lchild), check_height(root.rchild)) + 1  # 반환 대상 Integer


def improved_is_balanced(root):
    return check_height(root) != false_number


li = [1, 2, 3, 4, 5]
# bst
bst = create_bst(li, 0, 4)
print(is_balanced(bst))
print(improved_is_balanced(bst))
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
e = Node(4)
d.lchild = e
print(is_balanced(skewed_tree))
print(improved_is_balanced(skewed_tree))
