"""
https://www.acmicpc.net/problem/1914
하노이 탑
"""


def print_item(_from, to):
    print(f'{_from} {to}')


def hanoi(n, _from, by, to):
    if n == 1:
        print_item(_from, to)
    else:
        hanoi(n - 1, _from, to, by)
        print_item(_from, to)
        hanoi(n - 1, by, _from, to)


def hanoi_count(n):
    return (2 ** n) - 1


if __name__ == '__main__':
    n = int(input())
    print(hanoi_count(n))

    if n <= 20:
        hanoi(n, 1, 2, 3)

