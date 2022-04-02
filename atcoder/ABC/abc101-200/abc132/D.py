import math

MOD = 10 ** 9 + 7

n, k = map(int, input().split())

p = [0 for _ in range(n - k)]
p[0] = 1

q = [[0 for _ in range(n - k + 1)] for _ in range(n - k + 1)]
q[n - k][1] = 1
q[n - k][n - k] = 1
for i in range(2, n - k + 1):
    for r in range(2, i + 1):
        q[i][r] = q[i - 1][r - 1] + q[i - r][r]

print(q)
