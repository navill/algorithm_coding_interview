"""
단방향 연결리스트의 회문 여부 확인
0->1->2->1->0
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# 1.뒤집어서 비교
def is_palindrome(head):
    reversed_node = reversed_and_clone(head)
    return is_equal(head, reversed_node)


def reversed_and_clone(node):
    head = None
    while node:
        # tail이 아닌 head에 복사한 노드를 추가한다.
        n = Node(node.data)
        n.next = head
        # 헤드는 복사된 새로운 노드를 가리킨다.
        head = n
        node = node.next
    return head


def is_equal(n1, n2):
    while n1 and n2:
        if n1.data != n2.data:
            return False
        n1 = n1.next
        n2 = n2.next
    return n1 is None and n2 is None


# 2.순환적 접근 - fast & slow runner를 이용한다.
# slow가 중간에 도착할 떄 fast는 마지막 요소에 도착한다.
def is_palindrome_iter(h):
    fast = h
    slow = h
    stack = list()
    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next
    # 홀수 일 경우 위 순환문의 fast.next=None, fast=node가 된다.
    # 1,2,3,4,5(S),6,7,8,9(F) -> F.next = None
    # => S는 한개의 가운데 값이므로 비교 대상이 아니다.
    # 짝수 일 경우 fast.next=None, fast=None
    # 1,2,3,4,5(s),6,7,8,None(F)
    # => S는 가운데 값이지만 비교 대상이다(4와 5는 비교가 필요하다)
    if fast:
        slow = slow.next
    # 1,2,3,4(S),3,2,1(F)
    while slow:
        # stack = [1,2,3]
        # slow.data = 3
        top = stack.pop()
        if top != slow.data:
            return False
        slow = slow.next
    return True


# 3.재귀적 접근(page.312참고)
class Result:
    def __init__(self, node=None, result=False):
        self.node = node
        self.result = result


def is_palindrome_recur(h):
    size = node_size(h)
    res = recur(h, size)
    return res.result


def recur(h, size):
    # 짝수
    if size <= 0 or h is None:
        return Result(h, True)
    # 홀수
    if size == 1:
        # 2.Result(h.next, True) -> 3f를 건너 뛰고 2b를 Result에 담는다.
        return Result(h.next, True)

    # 0f, 1f, 2f, 3f(3b), 2b, 1b, 0b
    # 1. 재귀 -> 0부터 진행
    res = recur(h.next, size - 2)
    # 3. res.node=2b를 담고 있고, 현 시점에서 h.data는 2f를 담고 있음
    if res.node is None or res.result is False:  # 회문 결과 반환(값이 없고 res.result가 False일 경우)
        return res

    # 4. h.data(2f) == res.node.data(2b)
    res.result = (h.data == res.node.data)
    res.node = res.node.next  # res.node.next = 1b
    return res


def node_size(h):
    size = 0
    while h:
        size += 1
        h = h.next
    return size


head = Node(1)
node2 = Node(2)
head.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(2)
node3.next = node4
node5 = Node(1)
node4.next = node5
# node0 = Node(1)
# node5.next = node0
# is_palindrome(head)
print(is_palindrome_recur(head))
