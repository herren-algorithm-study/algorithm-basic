from itertools import permutations

N = int(input())
cost_matrix = [list(map(int, input().split())) for i in range(N)]
memo_ = [
    [1000001 for _ in range(N)]
    for _ in range(N)
]

result = float('inf')

cases = permutations([i for i in range(1, N)])
for case in cases:
    start = 0
    local_sum = 0
    continue_flag = False
    for city in case:
        cost = cost_matrix[start][city]
        if cost == 0:
            continue_flag = True
            break
        local_sum += cost
        start = city

    if continue_flag:
        continue

    if cost_matrix[start][0] == 0:
        continue

    local_sum += cost_matrix[start][0]

    if local_sum < result:
        result = local_sum

print(result)
