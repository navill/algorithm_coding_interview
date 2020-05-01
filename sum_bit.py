"""
덧셈 연산자 없이 두 개의 숫자 덧셈
bit 연산을 이용

A XOR B
 1001
^0011
=1010
두 비트가 서로 다를 때 1을 출력 -> 자릿수를 제외한 덧셈

A AND B
 1001
&0011
 0001 << 1
=0010
두 비트가 모두 1일 때 1을 출력 -> 자리올림 값 생성
"""


def sum_without_plus(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    _sum = a ^ b
    _carry = (a & b) << 1
    print(bin(_sum), '&', bin(_carry))
    return sum_without_plus(_sum, _carry)


print(sum_without_plus(9, 3))
