from collections import defaultdict

MOD = 998244353


class Facts:
    # O(max_num)
    def __init__(self, max_num: int = 10**5, p: int = 10**9 + 7) -> None:
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


n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == 0:
    print(1)
    exit()

# 偶数と奇数で変わる
# mod kの中の場合の数を求めると良い
ans = 0
ls = [[] for _ in range(k)]
for i in range(n):
    ai = a[i]
    ls[i % k].append(ai)

facts = Facts(max_num=n + 1, p=MOD)
# mod kの順列の場合の数を求める
perms = []
for num_list in ls:
    counter = defaultdict(int)
    for num in num_list:
        counter[num] += 1
    peri = facts.fact[len(num_list)]
    for v in counter.values():
        peri *= facts.rev[v]
        peri %= MOD
    perms.append(peri)
ans = 1
for peri in perms:
    ans *= peri
    ans %= MOD
print(ans)
