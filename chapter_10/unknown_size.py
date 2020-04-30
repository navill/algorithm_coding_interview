"""
크기를 알 수 없는 정렬된 배열에서 타겟 원소의 인덱스를 구하는 알고리즘

"""

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]


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
