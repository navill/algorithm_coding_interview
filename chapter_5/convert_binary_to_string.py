"""
0과 1 사이의 숫자를 이진수(문자열)로 변환하는 알고리즘
"""


# 1
def print_binary(num):
    if num >= 1 or num <= 0:
        return 'ERROR'
    li = list()
    li.append('0.')

    while num > 0:
        if len(li) > 32:
            return "ERROR"
        r = num * 2
        if r >= 1:
            li.append('1')
            num = r - 1
        else:
            li.append('0')
            num = r

    return ''.join(li)


print(print_binary(0.625))


# 2
def print_binary2(num):
    if num >= 1 or num <= 0:
        return 'ERROR'
    li = list()
    li.append('0.')
    frac = 0.5
    while num > 0:
        if len(li) > 32:
            return 'ERROR'
        if num >= frac:
            li.append('1')
            num -= frac
        else:
            li.append('0')
        frac /= 2
    return ''.join(li)


print(print_binary2(0.625))
