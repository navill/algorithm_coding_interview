from collections import Counter


# 1. 같은 문자가 몇 번나오는지 확인 - time complexity: O(N)
def palindrome(s):
    cnt = Counter(s)
    check = False
    for v in cnt.values():
        # 홀수개의 문자는 한 개만 존재할 수 있다.
        if v % 2 == 1:
            if check:
                # 홀수개의 문자가 한 번 더 나타날 경우 False를 반환한다.
                return False
            check = True
    return True


# 2. 비트연산 - O(N)
def palindrome_bit(s):
    bitvector = 0
    for i in s:
        # 해당 문자의 mask
        mask = 1 << (ord(i) - ord('a'))
        if bitvector & mask == 0:
            bitvector |= mask  # on
        else:
            bitvector &= ~mask  # off
        # bitvector & mask가 1일 경우 -> mask에 해당하는 문자는 홀수개 존재
    return True if bitvector & (bitvector - 1) == 0 or bitvector == 0 else False


"""
<1로 셋팅된 비트 확인>

00010000 - 1 = 00001111
00010000 & 00001111 = 0
0 => 전체 비트 중 한 개의 비트만 1로 셋팅됨을 의미

00010001 - 1 = 00010000
00010001 & 00010000 = 00010000
00010000 => 전체 비트 중 한 개 이상의 비트가 1로 셋팅됨을 의미 
"""

input_string = 'abcba'
print('입력문자:', input_string)
print(palindrome(input_string))
print(palindrome_bit(input_string))
