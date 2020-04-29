"""
아이가 n개의 계단을 오를 때, 아이는 1개, 2개, 3개의 계단을 오를 수 있다. 계단에 오르는 방법이 몇 가지가 있는가?

"""


def count_way(n, me):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif me[n] is not None:
        return me[n]
    else:
        me[n] = count_way(n - 1, me) + count_way(n - 2, me) + count_way(n - 3, me)
        return me[n]


def count_way_memo(n, me):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif me[n] is not None:
        return me[n]
    else:
        me[n] = count_way_memo(n - 1, me) + count_way_memo(n - 2, me) + count_way_memo(n - 3, me)
        return me[n]


n = 5
li = [None] * (n + 1)
print(count_way_memo(5, li))
