"""
https://www.acmicpc.net/problem/1978
"""


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    _i = 2
    while _i + _i <= n:
        if n % _i == 0:
            return False
        _i += 1
    return True


if __name__ == '__main__':
    int(input())
    prime_count = 0
    for i in (input()).split():
        if is_prime(int(i)):
            prime_count += 1
    print(prime_count)
