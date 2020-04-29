"""
정렬된 배열에서 a[i]=i인 값을 찾는 알고리즘 구현
"""


def magic_idx(li, start, end):
    if end < start:
        return -1
    mid = (start + end) // 2
    if li[mid] == mid:
        return mid
    elif li[mid] > mid:
        return magic_idx(li, start, mid - 1)
    else:
        return magic_idx(li, mid + 1, end)


#    [  0,   1,  2, 3, 4, 5, 6, 7, 8,  9, 10]
li = [-41, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
print(magic_idx(li, 0, 11))


# +문제: 만일 중복이 허용될 경우
def magic_idx_dup(li, start, end):
    if end < start:
        return -1
    mid = (start + end) // 2
    mid_value = li[mid]
    if li[mid] == mid:
        return mid
    left = magic_idx(li, start, min(mid - 1, mid_value))
    # left>=0일 경우 li[mid] == mid 값이 있다는 의미
    if left >= 0:
        return left
    # 그렇지 않을 경우 right -> 만일 li[end]까지 없을 경우 end<start = True => -1을 반환한다.
    right = magic_idx(li, max(mid + 1, mid_value), end)
    return right


li2 = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
print(magic_idx_dup(li2, 0, 11))
