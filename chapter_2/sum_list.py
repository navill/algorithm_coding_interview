"""
연결 리스트로 구성된 숫자의 합을 구하는 알고리즘
node1:1의 자리 -> node2:10의 자리-> node3:100의 자리
7->1->6 + 5->9->2 = 617 + 295 = 결과는 912(2->1->9)

"""

# linked list
from collections import deque


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# 7->1->6 + 5->9->2 = 7+5 -> (1)+1+9 -> (1)+6+2
# => 2 -> 1 -> 9
def sum_list(l1, l2, carry):
    if l1 is None and l2 is None:
        return None
    value = carry
    result = Node()
    if l1:
        value += l1.data
    if l2:
        value += l2.data
    result.data = value % 10

    if l1 is not None or l2 is not None:
        result.next = sum_list(None if l1 is None else l1.next, None if l2 is None else l2.next,
                               1 if value >= 10 else 0)
    return result


def test_sum_list(l1, l2, carry):
    if not l1 and not l2:
        return None
    value = carry
    result = Node()
    if l1:
        value += l1.data
    if l2:
        value += l2.data
    result.data = value % 10

    if l1 or l2:
        result.next = test_sum_list(l1.next if l1 else None, l2.next if l2 else None, 1 if value > 10 else 0)
    return result


head = Node(7)
node2 = Node(1)
head.next = node2
node3 = Node(6)
node2.next = node3
node0 = Node(6)
node3.next = node0

node4 = Node(5)
node5 = Node(9)
node4.next = node5
node6 = Node(2)
node5.next = node6

print(test_sum_list(head, node4, 0).data)
print(test_sum_list(head, node4, 0).next.data)
print(test_sum_list(head, node4, 0).next.next.data)
print(test_sum_list(head, node4, 0).next.next.next.data)