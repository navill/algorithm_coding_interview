"""
s1, s2가 주어졌을 때, s2가 s1을 회전시킨 결과임을 판멸하는 코드
ex) waterbottle -> erbottlewat
wat 이후 회전 -> wat을 맨 뒤로 이동 하면 erbottle + wat
x=wat
y=erbottle
xy = waterbottle
yx = erbottlewat
=> s1을 x와 y로 나눈 뒤 xy=s1이 되는지 + yx=s2가 되는지 확인
=> yx는 xy가 쪼개지는 지점에 상관없이 xyxy의 부분 문자열임
s2 in s1s1 = xyxy
"""


def is_rotation(s1, s2):
    length = len(s1)
    if length == len(s2) & length > 0:
        s1s1 = s1 * 2
        if s2 in s1s1:  # O(A+B)일 경우 is_rotation() -> O(N)
            return True
    return False


s1 = 'waterbottle'
s2 = 'erbottlewat'
print(is_rotation(s1, s2))

