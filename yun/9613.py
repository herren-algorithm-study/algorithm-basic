"""
https://www.acmicpc.net/source/16887929
"""

from itertools import combinations

def get_gcd(a, b):
  while b != 0:
    r = a%b
    a = b
    b = r
  return a

t = int(input())
for _ in range(t):
  numbers = list(map(int, input().split(' ')))[1:]
  print(sum([get_gcd(a,b) for a,b in combinations(numbers, 2)]))
