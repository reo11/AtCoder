MOD = 10**9 + 7


def rep_sqr(base, k):
    ans = 1
    while k > 0:
        if k & 1:
            ans = ans * base % MOD
        base = base * base % MOD
        k >>= 1
    return ans


n, k = map(int, input().split())

ans = 0
# 全てのgcdについて
gcd = [0 for i in range(k + 1)]
for i in reversed(range(1, k + 1)):
    d = k // i
    # i, 2i, 3i, ...を含めてd個
    gcd[i] = rep_sqr(d, n)
    # 倍数を上から削除
    j = i * d
    while j > i:
        gcd[i] -= gcd[j]
        j -= i
    ans += gcd[i] * i
    ans %= MOD

print(ans)
