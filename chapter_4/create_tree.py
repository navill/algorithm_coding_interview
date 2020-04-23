class Node:
    def __init__(self, node=None):
        self.node = node
        self.lchild = None
        self.rchild = None


def create_bst(li, left, right):
    if right < left:
        return None
    root_idx = (left + right) // 2
    node = Node(li[root_idx])
    node.lchild = create_bst(li, left, root_idx - 1)
    node.rchild = create_bst(li, root_idx + 1, right)

    return node


li = [1, 2, 3, 4, 5]

# print(create_bst(li, 0, 4))
