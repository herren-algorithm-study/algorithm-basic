"""
https://www.acmicpc.net/problem/1182
부분수열의 합
"""

from itertools import combinations


def solve(n1_list, n2_list):
    count = 0
    for i in range(1, n1_list[0] + 1):
        for item in combinations(n2_list, i):
            if sum(item) == n1_list[1]:
                count += 1
    return count


if __name__ == '__main__':
    n1_list = list(map(int, input().split()))
    n2_list = list(map(int, input().split()))
    print(solve(n1_list, n2_list))
