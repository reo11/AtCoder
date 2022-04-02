MOD = 1000000007
n, k = map(int, input().split())
a = list(map(int, input().split()))
tmp = a[:]
for i in range(k - 1):
    a.extend(tmp)
ans = 0
# 単調減少
for i in range(len(a) - 1):
    b = a[i]
    count = 0
    for j in range(i + 1, len(a)):
        if b > a[j]:
            count += 1
    ans += count
    ans %= MOD
print(ans)
