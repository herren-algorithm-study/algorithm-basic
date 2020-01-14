"""
https://www.acmicpc.net/source/16887833
"""

import sys
input = sys.stdin.readline
def get_prime_table(max):
  memo = [False, False, True] + [True for _ in range(max-2)]
  for i in range(4, max//2*2, 2):
    memo[i] = False
  d = 3
  while d*d <= max:
    if memo[d] == True:
      for i in range(d*d, max+1, d):
        memo[i] = False
    d += 2
  return memo

prime_table = get_prime_table(999999)

while True:
  n = int(input())
  if n == 0:
    break
  for odd in range(3,1000000,2):
    if prime_table[odd] and prime_table[n - odd]:
        print(f"{n} = {odd} + {n - odd}")
        break
