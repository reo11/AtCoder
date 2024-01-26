n, m = map(int, input().split())
MOD = 10**9 + 7


class Facts:
    def __init__(self, max_num=10**5, p=10**9 + 7):
        self.p = p
        self.max_num = max_num
        self.fact = [1] * (self.max_num + 1)
        self.rev = [1] * (self.max_num + 1)
        for i in range(1, self.max_num + 1):
            self.fact[i] = (self.fact[i - 1] * i) % self.p
        self.rev[self.max_num] = self.mod_pow(self.fact[self.max_num], self.p - 2)
        for i in range(self.max_num - 1, 0, -1):
            self.rev[i] = self.rev[i + 1] * (i + 1) % self.p

    def get_fact(self, n):
        return self.fact[n]

    def comb(self, n, k):
        if n < 0 or k < 0 or n < k:
            return 0
        if n == 0 or k == 0:
            return 1
        res = ((self.fact[n] * self.rev[k] % self.p) * self.rev[n - k]) % self.p
        return res

    def perm(self, n, k):
        if n < 0 or k < 0 or n < k:
            return 0
        if n == 0 or k == 0:
            return 1
        a = self.fact[n]
        b = self.fact[n - k]
        return (a * self.mod_pow(b, self.p - 2)) % self.p

    def mod_pow(self, a, b):
        ans = 1
        while b > 0:
            if b & 1:
                ans = ans * a % self.p
            a = a * a % self.p
            b >>= 1
        return ans


facts = Facts(max_num=5 * 10**5)

ans = 0
for k in range(n + 1):
    tmp = (-1) ** k
    tmp *= facts.comb(n, k) * facts.perm(m, k)
    tmp %= MOD
    tmp *= (facts.perm(m - k, n - k)) ** 2
    tmp %= MOD
    ans += tmp
    ans %= MOD
print(ans)
