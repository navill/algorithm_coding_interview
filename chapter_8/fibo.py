def fibonacci(n, me):
    if n == 0 or n == 1:
        return n
    if me[n] is None:
        me[n] = fibonacci(n - 1, me) + fibonacci(n - 2, me)
    return me[n]


li = [None] * 11

print(fibonacci(10, li))


def fibonacci2(n):
    if n == 0 or n == 1:
        return n
    return fibonacci2(n - 1) + fibonacci2(n - 2)


print(fibonacci2(10))


# def fibonacci3(n):
#     if n == 0 or n == 1:
#         return n
#     memo = [None] * n
#     memo[0] = 0
#     memo[1] = 1
#     for i in range(2, n):
#         memo[i] = memo[i - 1] + memo[i - 2]
#         print(memo[i])
#     return memo[n - 1] + memo[n - 2]


def fibonacci3(n):
    if n == 0 or n == 1:
        return n
    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a + b
    return a + b


print(fibonacci3(10))
