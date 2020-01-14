import math

cnt = 0
len = int(input())

arr = input().split()

for i in range (len):
    num = int(arr[i])
    
    check = (num != 1)
    
    for j in range(2, int(math.sqrt(num)) + 1):
        if num % j == 0:
            check = False
            break
    if check:
        cnt += 1
print(cnt)
