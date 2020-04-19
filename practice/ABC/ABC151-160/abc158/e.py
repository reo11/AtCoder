from collections import defaultdict

n, p = map(int, input().split())
s = list(map(int, list(input())))

ans = 0
if p == 2:
    for i in range(n):
        if s[i] % 2 == 0:
            ans += (i + 1)
elif p == 5:
    for i in range(n):
        if s[i] % 5 == 0:
            ans += (i + 1)
else:
    d = defaultdict(lambda: 0)
    ten = 1
    for i in reversed(range(n)):
        a = (s[i] * ten) % p
        d[i] = (d[i+1]+a) % p
        ten *= 10
        ten %= p

    cnt = defaultdict(lambda: 0)
    for i in reversed(range(n+1)):
        ans += cnt[d[i]]
        cnt[d[i]] += 1
print(ans)

