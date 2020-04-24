from chapter_4.create_tree import create_tree
from chapter_4.tree_traversal import in_order_traversal

"""
주어진 이진트리가 bst인지 검증하는 알고리즘
1. 중위 순회(중복된 값이 없을 경우)
2. 최소/최대 기법
"""

# 1. In-order traversal
index = 0


def verify_bst(node, li):
    global index
    if node is None:
        return
    # 중위 순회
    verify_bst(node.lchild, li)
    # 해당 노드(root)를 li에 저장
    li.append(node.node)
    # index += 1
    verify_bst(node.rchild, li)


def check_bst(node):
    li = list()
    verify_bst(node, li)

    for i in range(1, len(li)):
        if li[i] <= li[i - 1]:
            return False
    return True


last_value = None


def check_bst_2(node):
    global last_value
    if node is None:
        return True
    if check_bst_2(node.lchild) is False:
        return False
    # node가 None이거나 왼쪽 노드(last_value)가 오른쪽 노드(node.node)보다 클 경우
    if last_value and node.node <= last_value:
        return False

    last_value = node.node
    if check_bst_2(node.rchild) is False:
        return False
    return True


li = [1, 2, 3, 4, 5, 6, 7]
node = create_tree(li, 0, 6)
print(node.node)
print(check_bst(node))
print(check_bst_2(node))
in_order_traversal(node)

l = list()


def check_test(node):  # 1
    if node:
        check_test(node.lchild)  # 2
        l.append(node.node)
        check_test(node.rchild)  # 3
    print(l)


"""
        4
    2       6
1   3       5   7

! = root
!! = left
* = right
check_test(4) - root 
    (!)check_test(2)  # root=4
    |    (!)check_test(1)  # root=2
    |    |    (!)check_test(None)  # root=1.left
    |    |    |    if False: -> return
    |    |    l.append(1)  # [1]
    |    |    (*)check_test(None)  # root=1.right
    |    |    |    if False: -> return
    |    l.append(2)  # [1,2]
    |    (*)check_test(3)  # root=2
    |    |    (!)check_test(None)  # root=3.left
    |    |    |    if False: -> return
    |    |    l.append(1)  # [1,2,3]
    |    |    (*)check_test(None)  # root=3.right
    |    |    |    if False: -> return
    l.append(4)  # [1,2,3,4]
    (*)check_test(6)  # root=4
    |    (!)check_test(5)  # root=6.left    
    |    |    (!)check_test(None)  # root=5.left
    |    |    |    if False: -> return
    |    |    l.append(5)  # [1,2,3,4,5]
    |    |    (*)check_test(None)  # root=5.right
    |    |    |    if False: -> return
    |    l.append(6)  # [1,2,3,4,5,6]
    |    (*)check_test(7)  # root=6.right
    |         (!)check_test(None)  # root=7.left
    |         |    if False: -> return
    |         l.append(7)  # [1,2,3,4,5,6,7]
    |         (*)check_test(None)  # root=7.right
    |              if False: -> return
    |------- 재귀 종료        
    
"""                 

check_test(node)
