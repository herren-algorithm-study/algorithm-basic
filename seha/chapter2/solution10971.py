"""
https://www.acmicpc.net/problem/10971
외판원순회

1. 모든 path 조합을 추출
2. cost가 0이거나 sum_cost가 기존 min 값보다 큰 경우 계산 안함
3. min값 출력
"""
from itertools import permutations


def get_value(path, field, min_num):
    path += (path[0],)
    sum_cost = 0
    for i in range(len(path) - 1):
        if min_num < sum_cost:
            return -1
        if field[path[i]][path[i + 1]] == 0:
            return -1

        sum_cost += field[path[i]][path[i + 1]]

    return sum_cost


if __name__ == '__main__':
    n = int(input())

    field = []
    for _ in range(n):
        field.append(list(map(int, input().split())))

    min_num = float('inf')
    for num_list in permutations([i for i in range(n)], n):
        rst = get_value(num_list, field, min_num)
        if 0 < rst < min_num:
            min_num = rst
    print(min_num)
