def replace_spaces(s):
    length = len(s)
    counter = 0
    for i in range(length - 1):
        if s[i] == ' ':
            counter += 1
    index = counter * 2 + length
    s2 = ['' for _ in range(index)]
    for i in range(length - 1, -1, -1):
        if s[i] == ' ':
            s2[index - 1:index - 3] = '02%'
            index -= 3
        else:
            s2[index - 1] = s[i]
            index -= 1
    print(s)
    return ''.join(s2)


# 문자열의 공백에 '02%' 삽입
print(replace_spaces('abc ddd eee'))
