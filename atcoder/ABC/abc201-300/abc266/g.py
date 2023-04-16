MOD = 998244353


class Facts:
    # O(max_num)
    def __init__(self, max_num, p) -> None:
        self.p = p
        self.max_num = max_num
        self.fact = [1] * (self.max_num + 1)
        self.rev = [1] * (self.max_num + 1)
        for i in range(1, self.max_num + 1):
            self.fact[i] = (self.fact[i - 1] * i) % self.p
        self.rev[self.max_num] = self.mod_pow(self.fact[self.max_num], self.p - 2)
        for i in range(self.max_num - 1, 0, -1):
            self.rev[i] = self.rev[i + 1] * (i + 1) % self.p

    def comb(self, n: int, k: int) -> int:
        if n < 0 or k < 0 or n < k:
            return 0
        if n == 0 or k == 0:
            return 1
        res = ((self.fact[n] * self.rev[k] % self.p) * self.rev[n - k]) % self.p
        return res

    def comb_base(self, n: int, k: int) -> int:
        if n < 0 or k < 0 or n < k:
            return 0
        if n == 0 or k == 0:
            return 1
        a, b = 1, 1
        for i in range(k):
            a *= n - i
            a %= MOD
        for i in range(k):
            b *= k - i
            b %= MOD
        return (a * self.mod_pow(b, self.p - 2)) % self.p

    def perm(self, n: int, k: int) -> int:
        if n < 0 or k < 0 or n < k:
            return 0
        if n == 0 or k == 0:
            return 1
        a = self.fact[n]
        b = self.fact[n - k]
        return (a * self.mod_pow(b, self.p - 2)) % self.p

    def mod_pow(self, a: int, b: int) -> int:
        ans = 1
        while b > 0:
            if b & 1:
                ans = ans * a % self.p
            a = a * a % self.p
            b >>= 1
        return ans


r, g, b, k = map(int, input().split())
r -= k
g -= k

facts = Facts(3 * 10 ** 6, MOD)

ans = 1
ans *= facts.comb(g + b + k, g)
ans %= MOD
ans *= facts.comb(b + k, b)
ans %= MOD
ans *= facts.comb(k, k)
ans %= MOD

# Gの左隣以外ならどこでも入れられる
ans *= facts.comb(k + b + r, r)
ans %= MOD
ans *= facts.comb(k + b, k + b)
ans %= MOD
print(ans)
