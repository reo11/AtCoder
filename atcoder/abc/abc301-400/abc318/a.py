n, m, p = map(int, input().split())

ans = 0

for i in range(1, n + 1):
    if (i - m) % p == 0:
        ans += 1
print(ans)