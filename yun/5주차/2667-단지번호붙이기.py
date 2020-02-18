N = int(input())
board = []
directions = [(1, 0),  (0, 1), (0, -1), (-1, 0)]

group_count = 0
visited_tuples = {}

for _ in range(N):
    board.append(list(map(int, list(input()))))

for row in range(N):
    for col in range(N):
        if board[row][col] == 0:
            # 순회를 시작할 수 없음
            continue
        if (row, col) in visited_tuples:
            # 방문한 적 있으면 다시 순회할 필요 없음
            continue

        group_count += 1

        queue = [(row, col)]
        visited_tuples[(row, col)] = group_count

        while queue:
            node = queue.pop(0)
            for direction in directions:
                nrow = node[0] + direction[0]
                ncol = node[1] + direction[1]
                if nrow >= N or ncol >= N or nrow < 0 or ncol < 0:
                    continue
                if board[nrow][ncol] == 1 and (nrow, ncol) not in visited_tuples:
                    visited_tuples[(nrow, ncol)] = group_count
                    queue.append((nrow, ncol))

print(group_count)
counts = [0 for _ in range(group_count)]

for row in range(N):
    for col in range(N):
        try:
            counts[visited_tuples[(row, col)]-1] += 1
        except KeyError:
            continue

for count in sorted(counts):
    print(count)
