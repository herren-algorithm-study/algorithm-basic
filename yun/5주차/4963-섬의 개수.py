directions = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

while True:
    w, h = list(map(int, input().split(' ')))
    if (w, h) == (0, 0):
        break

    board = []
    visited_tuples = {}
    for _ in range(h):
        board.append(list(input().split(' ')))

    island_count = 0

    for row in range(h):
        for col in range(w):
            if board[row][col] == '0':
                # 바다에서는 순회를 시작할 수 없음
                continue
            if (row, col) in visited_tuples:
                # 방문한 적 있으면 다시 순회할 필요 없음
                continue

            # 여기서부터 순회 시작
            # print(f'순회시작, {row},{col}')

            island_count += 1

            queue = [(row, col)]
            visited_tuples[(row, col)] = island_count

            while queue:
                node = queue.pop(0)
                for direction in directions:
                    nrow = node[0]+direction[0]
                    ncol = node[1]+direction[1]
                    if nrow >= h or ncol >= w or nrow < 0 or ncol < 0:
                        continue
                    if board[nrow][ncol] == '1' and (nrow, ncol) not in visited_tuples:
                        visited_tuples[(nrow, ncol)] = island_count
                        queue.append((nrow, ncol))
    print(island_count)



