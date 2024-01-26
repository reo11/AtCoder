n, k = map(int, input().split())

MOD = 10**9 + 7

s = [0 for _ in range(n + 2)]
v = 0
for i in range(n + 2):
    v += i
    s[i] = v

ans = 0
for i in range(k, n + 2):
    t = (s[n + 1] - s[n + 1 - i]) - s[i] + 1
    ans += t
    ans %= MOD
print(ans)
