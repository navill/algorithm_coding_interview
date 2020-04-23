"""
최소 트리: 오름차순으로 정렬된 배열 안에 있는 정수를 이용해 높이가 최소가 되는 이진트리 생성
- 최소 트리가 되어야 하기 때문에 최하위(마지막 노드)는 루트를 기준으로 왼쪽과 오른쪽에 하나씩 동일하게 존재해야한다.
"""

tree_li = list()


class TreeNode:

    def __init__(self, root=None):
        self.root = root
        self.l_child = None
        self.r_child = None


def minimal_bst(li, left, right):
    if right < left:
        return None
    root_idx = (left + right) // 2
    node = TreeNode(li[root_idx])
    node.l_child = minimal_bst(li, left, root_idx - 1)
    node.r_child = minimal_bst(li, root_idx + 1, right)

    return node


li = [9, 8, 7, 6, 5, 4, 3, 2]
a = minimal_bst(li, 0, 7)


def pre_order_traversal(node, t):
    if node is None:
        return None
    print(node.root, end='->')
    pre_order_traversal(node.l_child, 1)
    pre_order_traversal(node.r_child, 2)


print('pre order traversal')
pre_order_traversal(a, 0)
# 5->8->9->7->6->3->4->2->1->
print('\n----------------------------')


def in_order_traversal(node, t):
    if node is None:
        return
    in_order_traversal(node.l_child, 1)
    print(node.root, end='->')
    in_order_traversal(node.r_child, 2)


print('in order traversal')
in_order_traversal(a, 0)
# 9->8->7->6->5->4->3->2->1->
