"""
https://www.acmicpc.net/problem/1072
게임
"""

x, y = map(int, input().split())

z = int(100 * y / x)
if z >= 99:
    print(-1)
else:
    a = x * (z + 1) - (100 * y)
    b = 99 - z
    div, mod = divmod(a, b)
    print(div + 1 if mod > 0 else div)
