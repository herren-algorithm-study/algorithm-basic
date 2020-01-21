import math
def get_z(x, y):
    return (y * 100) // x

try:
    while True:
        X, Y = map(int, input().split())
        z = get_z(X, Y)
        if z >= 99:
            print(-1)
            continue
        d = (100 * Y - z * X - X) / (z - 99)
        print(math.ceil(d))
except:
    exit(0)