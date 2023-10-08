MOD = 998244353

n, x = map(int, input().split())
t = list(map(int, input().split()))

class FLT:
    """
    フェルマーの小定理
    a^(-1) = a^(m-2) mod p
    """

    def __init__(self, mod: int = MOD) -> None:
        self.mod = mod

    def rep_sqr(self, base: int, k: int) -> int:
        ans = 1
        while k > 0:
            if k & 1:
                ans = ans * base % self.mod
            base = base * base % self.mod
            k >>= 1
        return ans

    def inv(self, a: int) -> int:
        """ 逆元を取る """
        return self.rep_sqr(a, self.mod - 2)

flt = FLT(MOD)
inv_n = flt.inv(n)
ans = 0
# 確率DP dp[i][j]: 時刻i丁度にj曲目が流れ終わった確率
dp = [[0 for _ in range(n + 1)] for _ in range(x + 2 * max(t) + 1)]
dp[0][0] = 1

for i in range(x + max(t)):
    for j in range(n):
        dp[i + t[j]][j + 1] = dp[i + t[j]][j + 1] + (dp[i][0] * inv_n)
        dp[i + t[j]][j + 1] %= MOD
    for j in range(1, n + 1):
        # 時刻i + 1丁度に任意の曲が流れ終わった確率
        dp[i + 1][0] += dp[i + 1][j]
        dp[i + 1][0] %= MOD

ans = 0
for i in range(x + 1, x + t[0] + 1):
    ans += dp[i][1]
    ans %= MOD
# print(dp)
print(ans)

