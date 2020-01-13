"""
https://www.acmicpc.net/problem/9613
"""


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == '__main__':
    for _ in range(int(input())):
        s, *num_list = map(int, input().split())
        cnt = 0
        for i in range(0, s - 1):  # 마지막수는 안돌아도 되기 때문에 s - 1
            for j in range(i + 1, s): # 끝까지 다 조합해봐야 됨. 단, 이전에 체크한건 다시 체크할 필요 없음
                rst = gcd(int(i), int(j))
                cnt += rst
                print(i, j, rst)
        print(cnt)
