N = int(input())


def is_hansoo(n: int):
    if n < 100:
        return True
    n = str(n)
    diff = int(n[1]) - int(n[0])
    for i in range(2,len(n)):
        local_diff = int(n[i]) - int(n[i-1])
        if local_diff != diff:
            return False
    return True

count = 0

for i in range(1, N+1):
    if is_hansoo(i):
        count += 1

print(count)