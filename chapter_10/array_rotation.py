"""
n개의 정수로 구성된 정렬상태(오름차순)의 배열을 임의의 횟수만큼 회전 -> 배열에서 특정 원소를 찾는 알고리즘

"""


def search(li, left, right, x):
    mid = (left + right) // 2
    if x == li[mid]:
        return mid
    if right < left:
        return -1

    # 왼쪽이 정상 정렬
    if li[left] < li[mid]:
        # 대상이 왼쪽(left와 mid사이)에 있을 경우
        if li[left] <= x < li[mid]:
            return search(li, left, mid - 1, x)
        else:
            return search(li, mid + 1, right, x)
    # 오른쪽이 정상 정렬
    elif li[left] > li[mid]:
        # 대상이 오른쪽(mid와 right사이)에 있을 경우
        if li[mid] < x <= li[right]:
            return search(li, mid + 1, right, x)
        else:
            return search(li, left, mid - 1, x)
    # mid와 left가 같을 경우
    elif li[left] == li[mid]:
        # mid와 right이 다를 경우
        if li[mid] != li[right]:
            # 오른쪽 탐색
            return search(li, mid + 1, right, x)
        # 아닐 경우 양쪽 탐색
        else:
            # 왼쪽 탐색
            result = search(li, left, mid - 1, x)
            if result == -1:
                # 없을 경우 오른쪽 탐색
                return search(li, mid + 1, right, x)
            else:
                return result
    return -1


li = [20, 25, 1, 2, 3, 4, 5, 14, 15, 16, 20]
print(search(li, 0, len(li) - 1, 20))
