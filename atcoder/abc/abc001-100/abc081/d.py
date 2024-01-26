n = int(input())
a = list(map(int, input().split()))
out = []


def solve_plus(out):
    for i in range(n - 1):
        out.append([i + 1, i + 2])
    return out


def solve_minus(out):
    for i in range(n - 1):
        out.append([n - i, n - i - 1])
    return out


max_a = 0
max_i = 0
min_a = 10**7
min_i = 0
for i in range(n):
    if a[i] > max_a:
        max_a = a[i]
        max_i = i + 1
    if a[i] < min_a:
        min_a = a[i]
        min_i = i + 1

if min_a >= 0:
    out = solve_plus(out)
elif max_a < 0:
    out = solve_minus(out)
else:
    if abs(max_a) > abs(min_a):
        for i in range(n):
            if a[i] < 0:
                out.append([max_i, i + 1])
        out = solve_plus(out)
    else:
        for i in range(n):
            if a[i] > 0:
                out.append([min_i, i + 1])
        out = solve_minus(out)
print(len(out))
for x, y in out:
    print(x, y)
