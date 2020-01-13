"""
https://www.acmicpc.net/problem/1934
"""


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a: int, b: int, gcd_ab: int) -> int:
    if gcd_ab:
        return divmod(a * b, gcd_ab)[0]
    return 0


if __name__ == '__main__':
    for _ in range(int(input())):
        a, b = map(int, input().split())
        print(lcm(a, b, gcd(a, b)))
