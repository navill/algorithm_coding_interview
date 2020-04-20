# from string import ascii_lowercase


def powers_of_2(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        prev = powers_of_2(n // 2)  # 수행시간은 한 번 실행될 때 마다 절반씩 줄어든다. -> O(logN)
        curr = prev * 2
        # 숫자가 출력될 때 마다 함수 실행을 의미
        print(curr)
        return curr


def power_of_2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        prev = power_of_2(n // 2)  # 50, 25, 12, 6, 3, 1, 0
        curr = prev * 2
        print(curr)
        return curr


power_of_2(50)
# for i in list(ascii_lowercase):
#     print(hash(i))
