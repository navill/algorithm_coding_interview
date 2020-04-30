"""
연산자를 사용하지 않고 정수 두개를 곱하는 재귀 함수
= 아직 이해가 안됨..
"""


# def min_product(a, b):
#     bigger = b if a < b else a
#     smaller = a if a < b else b
#     return min_product_helper(smaller, bigger)
#
#
# def min_product_helper(smaller, bigger):
#     if smaller == 0:
#         return 0
#     elif smaller == 1:
#         return bigger
#
#     s = smaller >> 1
#     side1 = min_product(s, bigger)
#     side2 = side1
#     if smaller % 2 == 1:
#         side2 = min_product_helper(smaller - s, bigger)
#
#     return side1 + side2
#
#
# print(min_product(5, 6))


def min_product2(a, b):
    bigger = b if a < b else a
    smaller = a if a < b else b
    return min_product_helper2(smaller, bigger)


def min_product_helper2(smaller, bigger):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger

    s = smaller >> 1
    half = min_product2(s, bigger)
    if smaller % 2 == 0:
        return half + half
    else:
        return half + half + bigger


print(min_product2(5, 6))