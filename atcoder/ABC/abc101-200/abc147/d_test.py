n = int(input())
a = list(map(int, input().split()))
MOD = 1000000007

ans = 0
for i in range(n-1):
    for j in range(i, n):
        ans += a[i] ^ a[j]
        ans %= MOD
print(ans)
