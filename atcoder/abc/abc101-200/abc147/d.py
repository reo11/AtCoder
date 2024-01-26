n = int(input())
a = list(map(int, input().split()))
MOD = 1000000007

bits = [0 for _ in range(60)]
for i in range(n):
    for b in range(60):
        if a[i] & 2**b > 0:
            bits[b] += 1

ans = 0
for i, b in enumerate(bits):
    if b > 0:
        ans += (2**i) * (b * (n - b))
        ans %= MOD
print(ans)
