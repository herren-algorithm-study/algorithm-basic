"""
https://www.acmicpc.net/problem/1065
한수
"""


def is_hansu(num: str):
    if len(num) > 2:
        gap = int(num[1]) - int(num[0])
        for i in range(2, len(num)):
            if int(num[i]) - int(num[i - 1]) != gap:
                return False
        return True
    else:
        return True


if __name__ == '__main__':
    count = 0
    for num in range(1, int(input()) + 1):
        if is_hansu(str(num)):
            count += 1
    print(count)
