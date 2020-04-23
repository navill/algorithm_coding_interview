class Node:
    def __init__(self, node=None):
        self.node = node
        self.lchild = None
        self.rchild = None


def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.lchild)
    print(node.node, end='->')
    in_order_traversal(node.rchild)


def pre_order_traversal(node):
    if node is None:
        return
    print(node.node, end='->')
    pre_order_traversal(node.lchild)
    pre_order_traversal(node.rchild)


def post_order_traversal(node):
    if node is None:
        return
    post_order_traversal(node.lchild)
    post_order_traversal(node.rchild)
    print(node.node, end='->')


"""
Node
       Root
    1       2
  3   4   5   6

"""
if __name__ == '__main__':
    root_node = Node('root')
    node1 = Node('1')
    node2 = Node('2')
    root_node.lchild, root_node.rchild = node1, node2
    node3 = Node('3')
    node4 = Node('4')
    node1.lchild, node1.rchild = node3, node4
    node5 = Node('5')
    node6 = Node('6')
    node2.lchild, node2.rchild = node5, node6
    pre_order_traversal(root_node)  # root->1->3->4->2->5->6
    print()
    print('----' * 5)
    in_order_traversal(root_node)  # 3->1->4->root->5->2->6
    print()
    print('----' * 5)
    post_order_traversal(root_node)  # 3->4->1->5->6->2->root
