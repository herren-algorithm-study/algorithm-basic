"""
https://www.acmicpc.net/problem/2609
"""


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a: int, b: int, gcd_ab: int) -> int:
    """
    lcm = (a * b) / gcd(a, b)
    """
    if a and b and gcd_ab:
        return divmod(a * b, gcd_ab)[0]
    return 0


if __name__ == '__main__':
    a, b = map(int, input().split())
    gcd_ab = gcd(a, b)
    print(gcd_ab)
    print(lcm(a, b, gcd_ab))
