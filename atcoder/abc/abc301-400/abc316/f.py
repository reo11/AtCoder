MOD = 998244353
n, a1, a2, a3 = map(int, input().split())

# x1 ^ x2 ^ x3 = 0
# つまり x1 ^ x3 = x2
# xは1 ~ n
# x1はa1の倍数, x2はa2の倍数, x3はa3の倍数
ans = 0
for x1 in range(a1, n + 1, a1):
    for x2 in range(a2, n + 1, a2):
        x3 = x1 ^ x2
        if 1 <= x3 and x3 <= n and x3 % a3 == 0:
            ans += 1
            # ans += max(x1, x2, x3) // n
print(ans)
