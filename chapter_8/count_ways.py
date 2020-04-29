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


def method1(n):
    li = [None] * (n + 1)
    return count_way_memo(n, li)


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


print(method1(5))


def method2(x):
    memo = [-1] * (x + 1)
    return triple_hop(x, memo)


def triple_hop(x, memo):
    if x < 0:
        return 0
    memo[0] = 1
    if x >= 1:
        memo[1] = 1
    if x >= 2:
        memo[2] = memo[1] + memo[0]
    if x > 2:
        for i in range(3, x + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[x]


print(method2(5))
