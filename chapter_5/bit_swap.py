"""
두 개의 정수를 2진수로 표현했을 때, A를 B로 변경하기 위해 뒤집어야하는 비트의 개수 구하기
두 숫자의 다른 비트를 찾기 -> XOR
ex)A:29(11101), B:15(01111)
C:10010
"""


def bin_swap(a, b):
    count = 0
    c = a ^ b

    while c != 0:
        # solution.1
        # count += c & 1
        # c >>= 1
        # solution.2
        c = c & (c - 1)  # 10010 & 10001
        count += 1
    return count


print(bin_swap(29, 15))
