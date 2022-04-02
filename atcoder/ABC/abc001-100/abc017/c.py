n, m = map(int, input().split())

s_sum = 0
scores = [0 for _ in range(m + 1)]
for i in range(n):
    l, r, s = map(int, input().split())
    s_sum += s
    scores[l - 1] += s
    scores[r] -= s

ans = 0
v = 0
for i in range(m):
    v += scores[i]
    ans = max(ans, s_sum - v)
print(ans)
