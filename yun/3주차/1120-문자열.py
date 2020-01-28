def calc_diff(x, y):
    result = len(x)
    for i in range(len(x)):
        if x[i] == '*' or y[i] == '*' or x[i] == y[i]:
            result -= 1
    return result

a, b = input().split()
diff = len(b) - len(a)

result_min = len(a)

for left in range(diff+1):
    prefix = '*'*left
    suffix = '*'*(diff - left)
    after_a = prefix + a + suffix
    local_result = calc_diff(after_a, b)
    if local_result < result_min:
        result_min = local_result
print(result_min)
