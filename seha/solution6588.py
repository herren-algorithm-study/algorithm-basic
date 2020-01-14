"""
https://www.acmicpc.net/problem/6588
"""

"""
4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
8 => 8 = 3 + 5, 20 => 3 + 17
만약, n을 만들 수 있는 방법이 여러 가지라면, b-a가 가장 큰 것을 출력한다
또, 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는 "Goldbach's conjecture is wrong."을 출력한다.

"""


def remove_num(num: int, num_field: list, bool_field: list):
    i = 2
    mul_num_i = num * i
    while True:
        if mul_num_i < len(num_field):
            if mul_num_i % 2 != 0:
                bool_field[int(mul_num_i / 2) - 1] = False
        else:
            break
        i += 1


def eratostenes_field(num_field: list, _bool_field) -> list:
    for i in range(len(num_field)):
        remove_num(num_field[i], num_field, _bool_field)

    return _bool_field


def find_match_num(prime_list: list, n: int):
    i, j = 0, len(prime_list) - 1
    while True:
        if prime_list[i] + prime_list[j] > n:
            j -= 1
        elif prime_list[i] + prime_list[j] < n:
            i += 1
        else:
            return prime_list[i], prime_list[j]


if __name__ == '__main__':
    num_field = []
    bool_field = []
    for i in range(3, 1000000, 2):
        num_field.append(i)
        bool_field.append(True)

    eratostenes_field(num_field, bool_field)

    while True:
        input_num = int(input())

        if input_num == 0:
            break

        prime_list = []
        for i in range(int(input_num / 2) - 1):
            if bool_field[i]:
                prime_list.append(num_field[i])

        a, b = find_match_num(prime_list, input_num)
        print(f'{input_num} = {a} + {b}')
