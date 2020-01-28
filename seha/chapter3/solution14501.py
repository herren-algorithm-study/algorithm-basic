"""
https://www.acmicpc.net/problem/14501
퇴사
"""

from functools import lru_cache


def sum_value(days, values):
    max_value = 0
    for j in range(len(days)):
        sum = 0
        i = j
        while i < len(days):
            # 지금날의 소요일 <= 남은일
            if days[i] <= len(days) - i:
                # sum에 더하고 jumping
                sum += values[i]
                i = i + days[i] + 1
                print(i)
            else:
                break

        if max_value < sum:
            max_value = sum

    return max_value


if __name__ == '__main__':
    days, values = [], []
    for i in range(int(input())):
        day, value = map(int, input().split())
        days.append(day)
        values.append(value)
