import sys

sys.setrecursionlimit(1000000)

MOD = 10 ** 9 + 7


class Facts:
    def __init__(self, max_num: int = 10 ** 5, p: int = 10 ** 9 + 7) -> None:
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


n, K = map(int, input().split())
facts = Facts()
node = [[] for _ in range(n)]
conect_count = [0 for _ in range(n)]
ans_num = [1 for _ in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    conect_count[a - 1] += 1
    conect_count[b - 1] += 1
    node[a - 1].append(b - 1)
    node[b - 1].append(a - 1)

checked = [False for _ in range(n)]


def dfs(num, pre_num):
    if checked[num]:
        return
    checked[num] = True

    if pre_num != -1 and len(node[num]) <= 1:
        return

    if pre_num == -1:
        ans_num[num] = (K * facts.perm(K - 1, len(node[num]))) % MOD
    else:
        ans_num[num] = facts.perm(K - 2, len(node[num]) - 1)

    for next_num in node[num]:
        dfs(next_num, num)


dfs(0, -1)
ans = 1
for a in ans_num:
    ans = (ans * a) % MOD

print(ans)
