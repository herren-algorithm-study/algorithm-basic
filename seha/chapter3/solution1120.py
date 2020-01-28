"""
https://www.acmicpc.net/problem/1120
문자열
"""

# 추가되는부분 셀 필요없음, 앞은 다 맞고 뒤만 확인
# 즉 n2 - n1 길이부터 탐색 시작
n1, n2 = map(str, input().split())
min_count = float('inf')
for i in range(len(n2) - len(n1) + 1):
    count = 0
    for j in range(len(n1)):
        if n1[j] != n2[i + j]:
            count += 1
    if count < min_count:
        min_count = count

print(min_count)
