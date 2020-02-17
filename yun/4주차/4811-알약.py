memo = {}


def solve(whole: int, half: int):
    global memo
    if whole == 0 and half == 0:
        return 1
    if whole < 0 or half < 0:
        return 0

    if (whole, half) in memo:
        return memo[(whole, half)]

    memo[(whole, half)] = solve(whole, half-1) + solve(whole-1, half+1)
    return memo[(whole, half)]


while True:
    N = int(input())
    if N == 0:
        break
    print(solve(N, 0))