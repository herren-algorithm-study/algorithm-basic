arr = []
for i in range(int(input())):
    list = input().split()
    index = int(list[0])
    sum = 0
    
    for j in range(index):
        for k in range(index - j - 1):
            a = int(list[j + 1])
            b = int(list[j + k + 2])

            min = a if a<b else b
            max = b if a<b else a
            while True:
                t = max % min
                if not t:
                    gcd = min
                    break
                else:
                    max = min
                    min = t
            sum += gcd
    
    arr.append(sum)

for i in arr:
    print(i)
