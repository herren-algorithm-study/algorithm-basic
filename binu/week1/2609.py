a, b = map(int,input().split())

min = a if a<b else b
for i in range(min):
    if a % (min - i) == 0 and b % (min - i) == 0:
        gcd = min - i
        break

print(gcd)
print(int(a*b/gcd))
