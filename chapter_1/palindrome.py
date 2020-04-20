from collections import Counter


# 1. 같은 문자가 몇 번나오는지 확인
def palindrome(s):
    cnt = Counter(s)
    check = False
    for v in cnt.values():
        if v % 2 == 1:
            if check:
                return False
            check = True
    return check


# 2. 비트연산
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


test_string = 'aahdmhjj'
print(palindrome(test_string))
print(palindrome_bit(test_string))

a = bin(ord('a') & (ord('a') - 1))
print(bin(ord('a') - 1))
print(bin(ord('b')))
print(a)
