def isuniqueuehars(s):
    if len(s) > 128:
        return False
    char_set = set()
    for i in s:
        val = i
        if val in char_set:
            return False
        char_set.add(val)
    return True


def isuniqueuechars_bit(s):
    checker = 0
    for i in s:
        val = ord(i) - ord('a')
        print(bin((1 << val) & checker))
        if ((1 << val) & checker) > 0:
            print(bin(checker))
            return False
        checker = (1 << val) | checker
        print('checker:', bin(checker))

    return True


print(isuniqueuechars_bit('abcdefa'))
"""
s[0] = a, val = 0, bin(1<<val) = 0b1, 1 << val & checker = 0
s[1] = b, val = 1, bin(1<<val) = 0b10, 1 << val & checker = 0
s[2] = c, val = 2, bin(1<<val) = 0b100, 1 << val & checker = 0
s[3] = d, val = 3, bin(1<<val) = 0b1000, 1 << val & checker = 0
s[4] = e, val = 4, bin(1<<val) = 0b10000, 1 << val & checker = 0
s[5] = f, val = 5, bin(1<<val) = 0b100000, 1 << val & checker = 0
s[6] = a, val = 0, bin(1<<val) = 0b1, 1 << val & checker = 1

key = char
value = char - 'a' 
{a:0,b:1,c:2,d:3,e:4,f:5,a:0}

1을 0칸 왼쪽으로 쉬프트  -> 1 -> checker(0)와 and 연산 -> checker = 0 
checker = (1 << val) | checker(0) -> 1
1을 1칸 왼쪽으로 쉬프트  -> 10 -> checker(1)와 and 연산 -> checker = 0
checker = (1 << val) | checker(1) -> 11
1을 2칸 왼쪽으로 쉬프트  -> 100 -> checker(11)와 and 연산 -> checker = 0
checker = (1 << val) | checker(11) -> 111
1을 3칸 왼쪽으로 쉬프트  -> 1000 -> checker(111)와 and 연산 -> checker = 0
checker = (1 << val) | checker(111) -> 1111
1을 4칸 왼쪽으로 쉬프트  -> 10000 -> checker(1111)와 and 연산 -> checker = 0
checker = (1 << val) | checker(1111) -> 11111
1을 5칸 왼쪽으로 쉬프트  -> 100000 -> checker(11111)와 and 연산 -> checker = 0
checker = (1 << val) | checker(11111) -> 111111
1을 0칸 왼쪽으로 쉬프트  -> 1 -> checker와(11111) and 연산 -> checker = 1
checker = (1 << val) | checker(1) -> 1
"""
