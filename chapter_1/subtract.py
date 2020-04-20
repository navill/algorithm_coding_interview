"""
두 개의 문자열 중 문자열을 같게 만들기 위한 편집 횟수가 1회 이내인지 확인하는 함수
교체, 삭제 <-> 삽입
삭제와 삽입은 한 개의 문자를 지우거나 삽입하기 때문에 동일한 logic에서 처리
=> 두 문자열 길이의 차이가 1보다 크지 않아야 한다.

time complexity - O(N) * N:길이가 짧은 문자열의 길이
두 문자열 중 길이가 짧은 문자열이 시간 복잡도를 좌우한다.
ex)
len(s1) = 1
len(s2) = 10
O(1)

len(s1) = 9
len(s2) = 10
O(9)

"""


# 1회 이내 True, 그렇지 않을 경우 False
def subtract(s1, s2):
    # 교체
    if len(s1) == len(s2):
        diff = False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                # 문자가 두 개 이상 다를 경우 diff는 True-> return False
                if diff:
                    return False
                diff = True
        return True
    # 삭제(또는 삽입)
    elif len(s1) - 1 == len(s2) or len(s1) + 1 == len(s2):
        idx1, idx2 = 0, 0
        while idx1 < len(s1) & idx2 < len(s2):
            if s1[idx1] != s2[idx2]:
                # 두 개 이상 문자가 다를 경우 아래의 조건문이 실행되면서 return False
                if idx1 != idx2:
                    return False
                idx2 += 1
            else:
                idx1 += 1
                idx2 += 1
        return True
    else:
        return False


print('[subtract]')
# 삭제
print(subtract('aple', 'apple'))
# 삽입
print(subtract('apple', 'aple'))
# 교체
print(subtract('bare', 'pare'))
# False - i와 h를 모두 변경해야한다.
print(subtract('ihhh', 'hihh'))


def subtract_second(s1, s2):
    # 문자열의 길이 차이가 1보다 작은지 확인 -> 삽입 또는 삭제 조건
    if abs(len(s1) - len(s2)) > 1:
        return False
    # s1은 짧은 문자열, s2는 긴 문자열
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    idx1, idx2 = 0, 0
    diff_check = False
    while (idx2 < len(s2)) & (idx1 < len(s1)):
        if s1[idx1] != s2[idx2]:
            if diff_check:
                return False
            diff_check = True
            # len(s1) == len(s2) : True => 교체
            if len(s1) == len(s2):
                # 교체 -> 문자열의 길이가 같을 경우 idx1++
                # 교체 시, else 이후에 idx2++을 함으로써 idx1과 idx2가 동일하게 증가한다.
                idx1 += 1
            # 삽입(또는 삭제) 시 문자열의 길이가 다르다.
            # ->idx1(짧은 문자)은 증가하지 않고 idx2(긴 문자)만 증가한다.
        else:
            idx1 += 1
        idx2 += 1
    return True


print('[subtract_second]')
# 삭제
print(subtract_second('aple', 'apple'))
# 삽입
print(subtract_second('apple', 'aple'))
# 교체
print(subtract_second('bare', 'pare'))
# False - i와 h를 모두 변경해야한다.
print(subtract_second('ihhh', 'hihh'))
