"""
https://www.acmicpc.net/source/16887079
"""

def get_gcd(a, b):
  while b != 0:
    r = a%b
    a = b
    b = r
  return a

def get_lcm(a, b):
  return a * b // get_gcd(a, b)

T = int(input())
for _ in range(T):
  a, b = map(int, input().split(' '))
  print(get_lcm(a, b))
