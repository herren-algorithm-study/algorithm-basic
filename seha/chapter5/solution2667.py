"""
https://www.acmicpc.net/problem/2667
단지번호 붙이기
"""


def dfs(i, j, danji_num):
    # 단지 0  아닐때마다 dict 카운트 올림
    if danji_num in danji_dict:
        danji_dict[danji_num] += 1
    else:
        danji_dict[danji_num] = 1

    danji_list[i][j] = 0
    visited[i][j] = True

    for k in range(4):
        if -1 < i + x[k] < danji_input_cnt and -1 < j + y[k] < danji_input_cnt:
            if danji_list[i + x[k]][j + y[k]] > 0 and not visited[i + x[k]][j + y[k]]:
                dfs(i + x[k], j + y[k], danji_num)


if __name__ == '__main__':
    danji_input_cnt = int(input())
    danji_list = [[int(i) for i in input()] for _ in range(danji_input_cnt)]
    visited = [[False for _ in range(danji_input_cnt)] for _1 in range(danji_input_cnt)]

    x = [0, 1, -1, 0]
    y = [1, 0, 0, -1]
    danji_dict = {}

    danji_num = 0
    for i in range(danji_input_cnt):
        for j in range(danji_input_cnt):
            if danji_list[i][j] > 0 and not visited[i][j]:
                dfs(i, j, danji_num)
                danji_num += 1

    print(len(danji_dict.keys()))
    for i in sorted(danji_dict.values()):
        print(i)
