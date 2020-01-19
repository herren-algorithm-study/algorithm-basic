from itertools import product

N = int(input())
original_board = [list(map(int, input().split())) for i in range(N)]

cases = []
for i in range(6):
    cases.extend(list(product([0, 1, 2, 3], repeat=i)))


def process_line(line):
    nonezero_line = [n for n in line if n != 0]

    if len(nonezero_line) == 0:
        return [0 for i in range(len(line))]

    for index in range(len(nonezero_line) - 1):
        if nonezero_line[index] == 0:
            continue
        if nonezero_line[index] == nonezero_line[index + 1]:
            nonezero_line[index] *= 2
            nonezero_line[index + 1] = 0

    nonezero_line = [n for n in nonezero_line if n != 0]
    return nonezero_line + [0 for i in range(len(line) - len(nonezero_line))]


def process_up(board, N):
    for col in range(N):
        line = [board[row][col] for row in range(N)]
        line = process_line(line)
        for row in range(N):
            board[row][col] = line[row]


def process_down(board, N):
    for col in range(N):
        line = [board[row][col] for row in range(N - 1, -1, -1)]
        line = process_line(line)
        for row in range(N):
            board[len(line) - 1 - row][col] = line[row]


def process_right(board, N):
    for row in range(N):
        line = [board[row][col] for col in range(N - 1, -1, -1)]
        line = process_line(line)
        for col in range(N):
            board[row][len(line) - 1 - col] = line[col]


def process_left(board, N):
    for row in range(N):
        line = [board[row][col] for col in range(N)]
        line = process_line(line)
        for col in range(N):
            board[row][col] = line[col]


def get_max(board):
    max = 0
    for row in board:
        for elem in row:
            if elem > max:
                max = elem
    return max


max_val = 0

for case in cases:
    b = [x[:] for x in original_board]
    for control in case:
        if control == 0:
            process_up(b, N)
        elif control == 1:
            process_down(b, N)
        elif control == 2:
            process_left(b, N)
        elif control == 3:
            process_right(b, N)
    local_max = get_max(b)
    if local_max > max_val:
        max_val = local_max
print(max_val)
