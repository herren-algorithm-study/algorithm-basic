from itertools import combinations
N, S = map(int, input().split())
a = list(map(int, input().split()))
result = 0
for length in range(1, N+1):
    subsequence = combinations(a, length)
    for seq in subsequence:
        if sum(seq) == S:
            result += 1
print(result)