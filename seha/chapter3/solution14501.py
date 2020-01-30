"""
https://www.acmicpc.net/problem/14501
퇴사
"""
from functools import lru_cache


@lru_cache(maxsize=None)
def sum_value(max_day, idx, sum, pre_sum):
    if idx == max_day:
        return sum
    if idx > max_day:
        return pre_sum
    a = sum_value(max_day, idx + 1, sum, sum)
    b = sum_value(max_day, idx + days[idx], sum + values[idx], sum)

    return max(a, b)


if __name__ == '__main__':
    max_day = int(input())
    days, values = [0] * max_day, [0] * max_day
    for i in range(max_day):
        days[i], values[i] = map(int, input().split())

    print(sum_value(max_day, 0, 0, 0))
