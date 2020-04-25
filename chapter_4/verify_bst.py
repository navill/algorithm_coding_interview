from chapter_4.create_tree import create_tree
from chapter_4.tree_traversal import in_order_traversal

l = list()


def check_test(node):
    if node:
        check_test(node.lchild)
        l.append(node.node)
        check_test(node.rchild)
    print(l)


"""
[node - BST]
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

# check_test(node)

"""
주어진 이진트리가 bst인지 검증하는 알고리즘
1. In-order traversal: 배열(list)에 중위순회 결과를 저장 
    => BST일 경우 배열에 저장된 값은 반드시 이전 값[i-1]이 이후[i]보다 작게 저장된다. 
2 최소 최대 기법: min & max value를 이용해 노드를 검사 
    => (max < node < min) 기준에 미치지 못할 경우 False 반환
"""
index = 0


# 1 In-order Traversal
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


"""
# 2 최소 최대 기법: min & max value를 이용해 노드를 검사 -> max <= node <min 기준에 미치지 못할 경우 False 반환
min & max
                20(r)
   None<[10]<20         20<[30]<None
(min <r.left<root)  (root<r.right<max)    
    
20을 기준으로
20.left -> min=None, max=20
20.right -> min=20, max=None 

def pseudo(n, min, max):
    if !n:
    # 재귀 시 아래의 조건들을 모두 만족하지 않고(False) 노드가 None이 될 경우 
    # True 반환   
        return True
    # root.node가 min&max 기준에 미치는지 확인
    if (!min and n.data<=min) or (!max and n.data>max):
        return False
    # 둘다 False가 아닐 경우
    # [min<n.left<n.data] or [n.data<n.right<max]
    if !pseudo(n.left, min, n.data) or !pseudo(n.right, n.data, max):  
        return False
    
    return True
"""


# 2 min & max
def check_bst_min_max(node, min=None, max=None):
    if node is None:
        return True

    if (min is not None and node.node <= min) or (max is not None and max < node.node):
        return False

    if check_bst_min_max(node.lchild, min, node.node) is False or check_bst_min_max(node.rchild, node.node,
                                                                                    max) is False:
        return False

    return True


print()

li_bst = [1, 2, 3, 4, 5, 6, 7]  # BST
node_bst = create_tree(li_bst, 0, 6)
li = [1, 2, 1, 4, 5, 6, 7]  # None BST
node = create_tree(li, 0, 6)

# 1-1: 중위 순회 방식
print('[li_bst] in order traversal:', end='')
in_order_traversal(node_bst)
print()
print('[li] in order traversal:', end='')
in_order_traversal(node)
print()
print(f'[li_bst] is BST?: {check_bst(node_bst)}')
print(f'[li] is BST?: {check_bst(node)}')
# 1-2: 중위 순회 방식(개선)
print(f'[li_bst] is BST?: {check_bst_2(node_bst)}')
print(f'[li] is BST?: {check_bst_2(node)}')
# 2: 최소 최대 방식
print(f'[li_bst] is BST?: {check_bst_min_max(node_bst)}')
print(f'[li] is BST?: {check_bst_min_max(node)}')
