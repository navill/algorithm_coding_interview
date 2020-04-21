"""
정렬되어있지 연결 리스트가 주어졌을 때 중복되는 원소 제거

"""


def remove_dups(li):
    hash_set = set()
    result = list()
    for i in li:
        if i not in hash_set:
            hash_set.add(i)
            result.append(i)
    return result


li = [5, 1, 2, 1, 3, 4, 5]
print(remove_dups(li))
