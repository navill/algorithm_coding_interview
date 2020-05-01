"""
크기를 알 수 없는 정렬된 배열에서 타겟 원소의 인덱스를 구하는 알고리즘

"""

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
"""
ex: target이 3일 때 
index=1(2), index=2(3) -> stop
left = 1, right = 2

target이 5일 때
index=1(2), index=2(3), index=4(5) -> stop
left = 2, right = 4 

target이 7일 때 
index=1(2), index=2(3), index=4(5), index=8(9) -> stop
left = 4, right = 8

=> 찾고자하는 대상은 반드시 index//2보다 큰 곳에 위치해 있다.
따라서 search함수가 실행될 때 left는 index//2가 된다.
"""


def search(li, x):
    index = 1
    # -1일 경우 타겟 원소의 크기가 index*2 이전에 포함되어 있다
    while li[index] != -1 and li[index] < x:
        index *= 2
    return binary_search(li, index // 2, index, x)


def binary_search(li, left, right, x):
    while left <= right:
        mid = (left + right) // 2
        mid_value = li[mid]
        if mid_value > x or mid_value == -1:
            right = mid - 1
        elif mid_value < x:
            left = mid + 1
        else:
            return mid
    return -1


print(search(li, 5))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def bi(a, x):
    left = 0
    right = len(a) - 1
    while left <= right:
        print('!')
        mid = (left + right) // 2
        if a[mid] > x:
            right = mid - 1
        elif a[mid] < x:
            left = mid + 1
        else:
            return mid


print(bi(a, 3))
