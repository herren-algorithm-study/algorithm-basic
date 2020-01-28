tc = int(input())

def find_larger(queue):
    for n in queue:
        if n[1] > queue[0][1]:
            return True
    return False

for _ in range(tc):
    N, M = tuple(map(int, input().split()))
    queue = [(index, priority) for index, priority in enumerate(map(int, input().split()))]
    target = queue[M]
    count = 0
    while True:
        if find_larger(queue):
            queue.append(queue[0])
            queue.pop(0)
        else:
            pop = queue.pop(0)
            if pop == target:
                print(count+1)
                break
            count += 1
