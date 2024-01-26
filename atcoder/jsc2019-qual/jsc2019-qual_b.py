MOD = 10**9 + 7
n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
# 単調減少
for i in range(n - 1):
    b = a[i]
    count = 0
    for j in range(i + 1, n):
        if b > a[j]:
            count += 1
    if count == 0:
        continue
    ap = k * (k + 1) // 2
    tmp = count * ap
    ans += tmp
    ans %= MOD

# それ以外
for i in range(n):
    b = a[i]
    count = 0
    for j in range(i):
        if b > a[j]:
            count += 1
    if count == 0:
        continue
    ap = (k - 1) * k // 2
    tmp = count * ap
    ans += tmp
    ans %= MOD
print(int(ans))
