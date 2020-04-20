# time complexity - fibonacci
# def fibo(n):  # O(2^N)
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibo(n - 1) + fibo(n - 2)
#
#
# for i in range(11):
#     # 반복문에서 fibo의 big-O는 2^i
#     # 2^1 + 2^2 + 2^3 + ... + 2^N
#     # => 2^(N+1)
#     print(fibo(i))

# 총 time complexity는 O(2^n)이 걸린다.


# time complexity - fibonacci with memoization


def fibo_m(n):
    if n == 0:
        return 0
    if n not in memo_li:  # O(1)
        memo_li[n] = fibo_m(n - 2) + fibo_m(n - 1)  # 조건문에 의해서 반복되지 않음 -> O(1)
    return memo_li[n]


"""
n=0, result=0, memo_li=[0,]
n=1, result=1, memo_li=[0,1,]
n=2, result=1, memo_li=[0,1,2]
n=3, result=2, memo_li=[0,1,2]
"""
memo_li = {0: 1, 1: 1}
for i in range(11):  # O(N)
    print(fibo_m(i))

print(list(memo_li.values()))
