n = int(input())


def func(a, b):
    return a**3 + a**2 * b + a * b**2 + b**3


ans = 10**18
j = 10**6
for i in range(10**6 + 1):
    while func(i, j) >= n and j >= 0:
        ans = min(func(i, j), ans)
        j -= 1
print(ans)
