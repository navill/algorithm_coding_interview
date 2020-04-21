"""
단방향 연결 리스트의 뒤에서 k번재 요소 찾기
재귀
비재귀
"""


# linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# recursive - TC:O(N), SC:O(N)
def nth_to_last_recur(node, k):
    if node is None:
        return 0
    index = nth_to_last_recur(node.next, k) + 1
    if index == k:
        print(k, 'th to last node is ', node.data)
        # return index, node.data
    return index


# iterative - TC:O(N), SC:O(1)
def nth_to_last_iter(node, k):
    p1 = node  # head
    p2 = node
    for _ in range(k):
        if p1 is None:
            return None
        p1 = p1.next  # p1을 k만큼 이동
    while p1 is not None:
        p1 = p1.next
        p2 = p2.next
    print(k, 'th to last node is ', p2.data)
    return p2


head = Node(1)
node2 = Node(2)
head.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(4)
node3.next = node4
node5 = Node(5)
node4.next = node5
nth_to_last_recur(head, 4)
nth_to_last_iter(head, 2)
