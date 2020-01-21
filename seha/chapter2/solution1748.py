"""
https://www.acmicpc.net/problem/1748
수 이어 쓰기1
"""
n = input()
x = len(n)

if x < 2:
    print(n)
else:
    rst = 9 + ((int(n) - (10 ** (x - 1))) + 1) * x
    rst += sum(((9 * (10 ** (i - 1))) * i) for i in range(2, x))
    print(rst)
