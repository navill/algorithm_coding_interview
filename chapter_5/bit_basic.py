# ckeck bit
def bit_check(num, i):
    """
    num의 i 번째 비트가 1인지 여부 확인
          4: 0100
       1<<2: 0100 (AND)
        res: True
    """
    return True if num & (1 << i) else False


print(bit_check(4, 2))


# set bit
def set_bit(num, i):
    """
    num에 i만큼 이동한 1비트를 삽입
       4: 0100
    1<<3: 1000 (OR)
     res: 1100 = 12
    """
    return num | (1 << i)


print(set_bit(4, 3))


# remove bit
def remove_bit(num, i):
    """
    num의 i번째 비트 삭제
        4: 0100
not(1<<3): 1011 (AND)
      res: 0000 = 0
    """
    mask = not (1 << i)
    return num & mask


print(remove_bit(4, 3))


# 최상위 비트부터 i번째 비트 삭제
def remove_bit_before_i(num, i):
    """
        num의 i번째 비트 삭제
            4: 0100
     (1<<2)-1: 0011 (AND)
          res: 0000 = 0

          최상위 비트부터 i번째 비트까지 모두 0이 되고, 하위 비트는 모두 1이 된다
          000000000(i)111111111
          => AND연산이 이뤄지면서 i 이전의 비트는 모두 삭제된다.
        """
    mask = (1 << i) - 1
    return num & mask


print('------' * 5)
"""
1의 개수 
해당 숫자 & 해당 숫자 - 1
=> 마지막 자리수가 뒤집힌다.
    11101
  & 11100
  = 11100  (세 개의 1이 남는다.)
위를 반복하면 해당 숫자의 1이 몇 개 인지 측정할 수 있다.
"""

a = 29  # (11101) -> 1의 개수가 총 4개
b = 21  # (10101) -> 1의 개수가 총 3개
while a:
    a = a & (a - 1)
    print(a)  # 28, 24, 16, 0 = 총 네 번 실행

while b:
    b = b & (b - 1)
    print(b)  # 20, 16, 0 = 총 세 번 실행

print('------' * 5)

print(remove_bit_before_i(4, 2))


# i번째 비트 이하 모든 비트 삭제
def remove_bit_after_i(num, i):
    """
        num의 i번째 비트 삭제
             4: 0100
     (-1<<2+1): 1111 -> 1000 (AND)
        4: 0100
           1000 (AND)
      res: 0100 = 0

          i(4)번째 비트 ~ 0번째 비트 삭제
          1111(i+1)0000
          => AND연산이 이뤄지면서 i 이하의 비트는 모두 삭제된다.
    """
    mask = -1 << (i + 1)
    return num & mask


print(remove_bit_after_i(4, 2))


# 비트값 바꾸기
def change_bit(num, i, bit_is_1):
    value = 1 if bit_is_1 else 0
    mask = not (1 << i)  # i(3): 11110111 -> 네 번째 비트를 제외한 나머지는 1
    # i 번째 비트를 0으로 변경한 후 or (value << i)
    return (num and mask) or (value << i)
