MOD = 998244353
n, a, b, p, q = map(int, input().split())

class FLT:
    def __init__(self, mod) -> None:
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

flt = FLT(mod=MOD)

# i(0<=i<=100)手目までにマス目j(0<=j<=100)にたどりついている確率
dpa = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
dpb = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
# 高橋君の初期地点
dpa[0][a] = 1
# 青木君の初期地点
dpb[0][b] = 1

# 高橋君の分
for i in range(1, n + 1):
    for j in range(1, n):
        # jから移動する
        r_sum = 0
        for k in range(j + 1, min(j + 1 + p, n + 1)):
            if k == min(j + p, n):
                dpa[i][k] += (dpa[i - 1][j] * flt.inv(p) * (p - r_sum)) % MOD
            else:
                dpa[i][k] += (dpa[i - 1][j] * flt.inv(p)) % MOD
                r_sum += 1

# 青木君の分
for i in range(1, n + 1):
    dpb[i][-1] = dpb[i - 1][-1]
    for j in range(1, n):
        # jから移動する
        r_sum = 0
        for k in range(j + 1, min(j + 1 + q, n + 1)):
            if k == min(j + q, n):
                dpb[i][k] += (dpb[i - 1][j] * flt.inv(q) * (q - r_sum)) % MOD
            else:
                dpb[i][k] += (dpb[i - 1][j] * flt.inv(q)) % MOD
                r_sum += 1

# 勝率を累積していく
ans = 0
for i in range(1, n + 1):
    # i手目で高橋君が勝利している確率
    # x = i手目でnマスに高橋君がいる確率
    # y = i - 1手目にnマスに青木君がいない確率
    # x * y
    ans = (ans + dpa[i][-1] * (1 - dpb[i - 1][-1])) % MOD

print(ans)
# pprint.pprint(dpa)
# pprint.pprint(dpb)
