"""
https://www.acmicpc.net/source/16886704
"""

N = int(input())
numbers = map(int, input().split(' '))

def is_prime(n):
  if n < 2:
    return False
  d = 2
  while d*d <= n:
    if n % d == 0:
      return False
    d += 1
  return True

print(len([x for x in numbers if is_prime(x)]))
