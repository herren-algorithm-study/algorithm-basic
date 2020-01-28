from itertools import product

N, M = tuple(map(int, input().split()))
office = [list(map(int, input().split())) for i in range(N)]

rotate_constant = [None, 4, 2, 4, 4, 1, None]

cctv_info = []

for col in range(N):
    for row in range(M):
        if 6 > office[col][row] > 0:
            cctv_info.append((office[col][row], col, row))

rotate_cases = list(product(*[list(range(rotate_constant[n])) for n, _, __ in cctv_info]))


def fill_line(office, start_col, start_row, direction):
    if direction == 0:
        if start_col == 0:
            return
        for col in range(start_col - 1, -1, -1):
            if office[col][start_row] == 0:
                office[col][start_row] = '#'
            elif office[col][start_row] == 6:
                break
    elif direction == 1:
        if start_row == M - 1:
            return
        for row in range(start_row + 1, M):
            if office[start_col][row] == 0:
                office[start_col][row] = '#'
            elif office[start_col][row] == 6:
                break
    elif direction == 2:
        if start_col == N - 1:
            return
        for col in range(start_col, N):
            if office[col][start_row] == 0:
                office[col][start_row] = '#'
            elif office[col][start_row] == 6:
                break
    elif direction == 3:
        if start_row == 0:
            return
        for row in range(start_row - 1, -1, -1):
            if office[start_col][row] == 0:
                office[start_col][row] = '#'
            elif office[start_col][row] == 6:
                break
    else:
        raise Exception("Unexpected direction")


def calculate_area(office):
    count = 0
    for col in range(N):
        for row in range(M):
            if office[col][row] == 0:
                count += 1
    return count


def pprint(office):
    global N, M
    for col in range(N):
        for row in range(M):
            print(office[col][row], end=' ')
        print('')


min_area = 65

for case in rotate_cases:
    lo = [x[:] for x in office]  # local office
    for (cctv_type, cctv_col, cctv_row), rotate in zip(cctv_info, case):
        if cctv_type == 1:
            fill_line(lo, cctv_col, cctv_row, rotate)
        elif cctv_type == 2:
            fill_line(lo, cctv_col, cctv_row, rotate)
            fill_line(lo, cctv_col, cctv_row, (rotate + 2) % 4)
        elif cctv_type == 3:
            fill_line(lo, cctv_col, cctv_row, rotate)
            fill_line(lo, cctv_col, cctv_row, (rotate + 1) % 4)
        elif cctv_type == 4:
            fill_line(lo, cctv_col, cctv_row, (rotate + 1) % 4)
            fill_line(lo, cctv_col, cctv_row, (rotate + 2) % 4)
            fill_line(lo, cctv_col, cctv_row, (rotate + 3) % 4)
        elif cctv_type == 5:
            fill_line(lo, cctv_col, cctv_row, 0)
            fill_line(lo, cctv_col, cctv_row, 1)
            fill_line(lo, cctv_col, cctv_row, 2)
            fill_line(lo, cctv_col, cctv_row, 3)
    calculated_area = calculate_area(lo)
    if calculated_area < min_area:
        min_area = calculated_area

print(min_area)
