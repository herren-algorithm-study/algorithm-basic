"""
https://www.acmicpc.net/problem/11729
하노이탑 이동순
"""

arr = []


def add_item(_from, to):
    arr.append(f'{_from} {to}')


def hanoi(n, _from, by, to):
    if n == 1:
        add_item(_from, to)
    else:
        hanoi(n - 1, _from, to, by)
        add_item(_from, to)
        hanoi(n - 1, by, _from, to)


if __name__ == '__main__':
    hanoi(int(input()), 1, 2, 3)
    print(len(arr))
    if len(arr) < 20:
        [print(item) for item in arr]
