from math import gcd, sqrt

"""
모든 수는 소수의 곱으로 나타낼 수 있음
gcd(x,y) = 2^min(j0, k0), 3^min(j1, k1), 5^min(j2, k2), ...
lcm(x,y) = 2^max(j0, k0), 3^max(j1, k1), 5^max(j2, k2), ... 
gcd * lcm = x * y
lcm = (x * y) // gcd
"""


def prime(num):
    if num < 2:
        return False
    i = 2
    while i < num:
        if (num % i) == 0:
            return False
        i += 1
    return True


def prime_better(num):
    if num < 2:
        return False
    i = 2
    sqrt_num = int(sqrt(num))
    while i < sqrt_num:
        if (num % i) == 0:
            return False
        i += 1
    return True


print(prime(13))
print(prime_better(13))

"""
에라토스테네스의 체: 소수 목록을 만드는 방법
1. 1~max가 담긴 배열에서 에서 2의 배수를 제거(해당 배열 False)
2. 그다음 가장 작은 소수(3)의 배수를 제거
3. 그다음 가장 작은 소수(5)의 배수를 제거... 반복

"""


def sieve_of_eratosthenes(max):
    flags = [True for _ in range(max)]
    flags[0] = False
    flags[1] = False
    prime = 2
    while prime <= int(sqrt(max)):
        cross_off(flags, prime)
        prime = get_next_prime(flags, prime)
    return flags


# flags에 있는 prime의 배수 제거(False)
def cross_off(flags, prime):
    i = prime * prime
    # prime 배수 제거
    while i < len(flags):
        flags[i] = False
        i += prime


# 다음 소수
def get_next_prime(flags, prime):
    next = prime + 1
    # flags[next]=True(cross_off에 의해 제거되지 않은 flags)일 경우 next 반환
    while next < len(flags) & flags[next] is False:
        next += 1
    return next


result = sieve_of_eratosthenes(100000)
prime_numbers = [i for i, v in enumerate(result) if v is True]


def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] is True:
            for j in range(i + i, n, i):  # i의 배수만큼 증가
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] is True]


a = prime_list(100000)
print(len(a))
print(len(prime_numbers))
if a == prime_numbers:
    print('!!')


def prime_test(n):
    sieve = [True] * n
    m = int(sqrt(n))
    for i in range(2, m + 1):
        if sieve[i] is True:
            for j in range(i * i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] is True]


c = prime_test(100000)
print(c == a == prime_numbers)
