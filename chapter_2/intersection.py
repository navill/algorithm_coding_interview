"""
단방향 리스트 두개가 주어졌을 때 교집합 노드(노드의 주소가 겹치는 노드)를 찾아 반환
3->1->5->9->7->2->1
      4->6->7(위와 동일한 노드 객체)

3->1->5->9->7->2->1
      4->6->7->2->1(위와 다른 노드 객체들)

[1.교집합 유무 판별]
1. 노드(의 주소)를 해쉬 테이블에 넣어서 동일한 값이 있는지 확인
2. 두 리스트에 교집합이 존재할 경우 마지막 노드는 동일한 identify를 갖는다
    -> 순회 후 마지막 노드의 identify를 비교

[2.겹치는 노드 찾기]
두 리스트의 길이가 같을 경우
1. True일 경우 -> 동시에 순회하면서 같은 값을 찾는다.
길이가 다를 경우
-> 두 리스트의 차를 구하고 그 차만큼 짧은 리스트의 앞부분을 무시

[3. 통합]
1. 각 리스트를 순회하면서 마지막 노드와 길이를 구한다.
2. 마지막 노드 비교 -> 서로 다를 경우 교집합이 아님 -> return False
3. 길이가 더 긴 리스트를 두 리스트 길이의 차만큼 앞으로 이동
4. 순회하면서 값이 같은지 확인
List1 의 길이:A
List2 의 길이:B
TC: O(A+B)
SC: O(1)
"""


class Result:
    def __init__(self, tail=None, size=0):
        self.tail = tail
        self.size = size


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def find_intersection(list1, list2):
    result1 = get_tail_and_size(list1)
    result2 = get_tail_and_size(list2)
    # 1-2 교집합 유무 판별
    if result1.tail is not result2.tail:
        return False
    short = list1
    long = list2
    # shorter = list1, longer = list2 정의
    if result1.size > result2.size:
        short, long = list2, list1

    # 2.겹치는 노드 찾기: 길이가 긴(result2)의 앞부분을 k만큼 이동한 result2를 반환한다.
    long = get_kth_node(long, abs(result2.size - result1.size))
    # 3-4 순회하면서 동일값 찾기
    # 동일한 값이 result에 저장되어있을 때 -> return result1(또는 result2)
    while short.data != long.data:
        short = short.next
        long = long.next

    return long


# 마지막 노드와 리스트의 사이즈 확인
def get_tail_and_size(li):
    if li is None:
        return False
    size = 1
    current = li
    while current.next:
        size += 1
        current = current.next
    return Result(tail=current, size=size)


# 길이가 긴 리스트의 앞부분을 자르기 위한 함수
def get_kth_node(head, size):
    current = head
    while size > 0 and current:
        current = current.next
        size -= 1
    # 이동한 노드를 반환
    return current


# 3->1->5->9->7->2->1
#       4->6->7(위와 동일한 노드 객체)

node1 = Node(3)
node2 = Node(1)
node1.next = node2
node3 = Node(5)
node2.next = node3
node4 = Node(9)
node3.next = node4
node5 = Node(7)
node4.next = node5
node6 = Node(2)
node5.next = node6
node7 = Node(1)
node6.next = node7

s_node1 = Node(4)
s_node2 = Node(6)
s_node1.next = s_node2
s_node2.next = node5

result = find_intersection(s_node1, node1)
if result:
    print('intersection node:', result.data)
else:
    print('not found intersection')
