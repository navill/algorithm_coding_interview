"""
쌍끼리 맞바꾸기: 짝수번째 비트와 홀수 번째 비트를 맞바꾸기

"""


def swap_odd_even_bits(n):
    mask_even = 0xAAAA
    mask_odd = 0x5555
    # &, | 연산과 shift 연산에 대한 구분을 명확히 해야함(괄호가 없을 경우 다른 결과)
    even = (n & mask_even) >> 1
    odd = (n & mask_odd) << 1
    return even | odd


print(swap_odd_even_bits(10))  # input: 10(1010)
# result: 5(0101)
