import math

check = [0] * 1000000

arr = [3]
ret = []

def is_decimal(num):
    global check

    if check[num] == 1:
        return True
    elif check[num] == -1:
        return False
    else:
        chk = (num != 1)

        for j in range(2, int(math.sqrt(num)) + 1):
            if num % j == 0:
                chk = False
                break
        if chk:
            check[num] = 1
            return True
        else:
            check[num] = -1
            return False

if __name__ == '__main__':
    while True:
        num = int(input())
        if num == 0:
            break

        find = False

        for i in arr:
            if is_decimal(num - i):
                ret.append(f'{num} = {i} + {num - i}')
                find = True
                break
        
        if not find:
            while i < num:
                i = i + 2
                
                if is_decimal(i) and is_decimal(num - i):
                    ret.append(f'{num} = {i} + {num - i}')
                    find = True
                    break
        if not find:
            ret.append("Goldbach's conjecture is wrong.")
    for str in ret:
        print(str)        
