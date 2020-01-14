arr = []
for i in range(int(input())):
    a, b = map(int,input().split())
    
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
    
    arr.append(int(a*b/gcd))

for i in arr:
    print(i)
