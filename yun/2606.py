"""
https://www.acmicpc.net/source/16886868
"""

a, b = map(int, input().split(' '))

def get_gcd(a, b):
  while b != 0:
    r = a%b
    a = b
    b = r
  return a

gcd = get_gcd(a, b)

print(gcd)
print(a*b//gcd)
