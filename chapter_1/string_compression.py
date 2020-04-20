"""
문자열 압축 코드
abbbbbbcaaaccc -> a1b6c1a3c3
만일 압축된 문자열의 길이가 원래 문자열 길이보다 길 경우 원래 문자 반환
abcaba -> abcaba

"""


def string_comp(s):
    length = len(s)  # lenght = 9
    result_list = list()
    counter = 0
    for i in range(length):
        counter += 1  # max_i = 8
        if i + 1 >= length or s[i] != s[i + 1]:
            # result_str += str(s[i]) + str(counter)
            # 문자열을 하나씩 더할 경우 O(p+k^2)의 시간이 걸린다.
            # p: 문자열의 길이, k: 반복되는 문자 개수
            # 문자열을 합치는데 O(n^2)의 시간이 걸림
            result_list.append(str(s[i]))
            result_list.append(str(counter))
            counter = 0
    result = ''.join(result_list)
    return s if length < len(result) else result


print(len('abca'))
print(string_comp('abbbbbbcaaaccc'))
print(string_comp('abcaba'))
