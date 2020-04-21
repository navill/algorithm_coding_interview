"""
단방향 연결 리스트에 값 x가 주어졌을 때 x보다 작은 모든값을 왼쪽으로 이동
큰값은 어디든 위치할 수 있음
"""


# linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def partition(node, x):
    before_start = None
    before_end = None
    after_start = None
    after_end = None
    # 노드 분할
    while node:
        node_next = node.next
        node.next = None
        if node.data < x:
            # 노드가 비어있을 경우
            if before_start is None:
                before_start = node
                before_end = before_start
            else:
                # 마지막에 노드를 추가
                before_end.next = node
                before_end = node
        # target은 after node에 포함된다.
        else:
            # 노드가 비어있을 경우
            if after_start is None:
                after_start = node
                after_end = after_start
            else:
                # 마지막에 노드를 추가
                after_end.next = node
                after_end = node
        node = node_next
    if before_start is None:
        return after_start
    # before start --- before end --- target --- after start --- after end
    before_end.next = after_start
    return before_start


def partition2(node, target):
    gt_li = list()
    ls_li = list()
    while node:
        if node.data < target:
            ls_li.append(node.data)
        else:
            gt_li.append(node.data)
        node = node.next
    ls_li += gt_li
    return ls_li


node1 = Node(8)
node2 = Node(6)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(2)
node3.next = node4
node5 = Node(1)
node4.next = node5

# a = partition(node1, 2)

# print(a.data)
# print(a.next.data)
# print(a.next.next.data)
# print(a.next.next.next.data)
# print(a.next.next.next.next.data)

b = partition2(node1, 2)
print(b)
