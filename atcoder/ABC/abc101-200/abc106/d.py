import sys

input = sys.stdin.buffer.readline

n, m, q = map(int, input().split())

counts = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    l, r = map(int, input().split())
    counts[l][r] += 1

s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

# 横方向
for i in range(n + 1):
    v = 0
    for j in range(n + 1):
        v += counts[i][j]
        s[i][j] = v

ans = []
for i in range(q):
    p, q = map(int, input().split())
    t = 0
    for i in range(p, q + 1):
        t += s[i][q] - s[i][p - 1]
    ans.append(str(t))
print("\n".join(ans))
