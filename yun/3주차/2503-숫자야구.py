from itertools import permutations

def calc_strike_ball(answer: str, guess: str):
    strike, ball = 0, 0
    for index, digit in enumerate(guess):
        if digit == answer[index]:
            strike += 1
        elif digit in answer:
            ball += 1
    return strike, ball

N = int(input())
rules = [tuple(map(int, input().split())) for _ in range(N)]

answer = 0

for testcase in permutations([str(x) for x in range(1, 10)], 3):
    match_count = 0

    for rule in rules:
        if calc_strike_ball(testcase, str(rule[0])) == (rule[1], rule[2]):
            match_count += 1

    if match_count == N:
        answer += 1
print(answer)
