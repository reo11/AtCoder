n, m = map(int, input().split())
a = list(map(int, input().split()))

# 累積和
def cumsum(a):
    r = [0]
    for v in a:
        r.append(r[-1] + v)
    return r


cumsum_a = cumsum(a)

ans = -float("inf")

v = 0
# 初期状態
for i in range(m):
    v += a[i] * (i + 1)
ans = max(ans, v)

for i in range(1, n - m + 1):
    sub = cumsum_a[i + m - 1] - cumsum_a[i - 1]
    v = v - sub + (a[i + m - 1] * m)
    ans = max(ans, v)
print(ans)
