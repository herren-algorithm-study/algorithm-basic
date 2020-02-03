"""
https://www.acmicpc.net/problem/1966
프린터 큐
"""
# n = 총 갯수, m = 위치(0부터)
# mutable_list = 유동적인 리스트
# index_list = index 추적을 위한 리스트
# sequence_list = 출력순서 저장
for _ in range(int(input())):
    n, m = map(int, input().split())
    rank_list = [int(i) for i in input().split()]
    mutable_list = rank_list.copy()
    index_list = [i for i in range(n)]

    cnt = 1
    while index_list:
        if rank_list[index_list[0]] == max(mutable_list):
            current_index = index_list.pop(0)
            if current_index == m:
                break

            mutable_list.remove(max(mutable_list))
            cnt += 1
        else:
            index_list.append(index_list.pop(0))
    print(cnt)
