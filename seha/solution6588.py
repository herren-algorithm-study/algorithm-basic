"""
https://www.acmicpc.net/problem/6588

4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
8 => 8 = 3 + 5, 20 => 3 + 17
만약, n을 만들 수 있는 방법이 여러 가지라면, b-a가 가장 큰 것을 출력한다
또, 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는 "Goldbach's conjecture is wrong."을 출력한다.

"""


def eratostenes_field() -> list:
    _bool_field = [True for _ in range(SIZE)]

    for i in range(2, SIZE):
        if i * i > SIZE - 1:
            break
        if _bool_field[i]:
            # 배수 false
            for j in range(i * i, SIZE, i):
                _bool_field[j] = False
    return _bool_field


if __name__ == '__main__':
    SIZE = 1000001
    bool_field = eratostenes_field()
    while True:
        input_num = int(input())

        if input_num == 0:
            break

        for i in range(2, SIZE):
            if bool_field[i]:
                j = input_num - i
                if bool_field[j]:
                    print(f'{input_num} = {i} + {j}')
                    break
