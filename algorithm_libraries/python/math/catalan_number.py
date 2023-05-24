class Facts:
    # O(max_num)
    def __init__(self, max_num: int = 10 ** 5, p: int = 10 ** 9 + 7) -> None:
        self.p = p
        self.max_num = max_num * 2
        self.fact = [1] * (self.max_num + 1)
        for i in range(1, self.max_num + 1):
            self.fact[i] = self.fact[i - 1] * i
            self.fact[i] %= self.p

    def comb(self, n: int, k: int) -> int:
        # nCk mod p with memo
        # O(log(p))
        if n < 0 or k < 0 or n < k:
            return 0
        if n == 0 or k == 0:
            return 1
        a = self.fact[n]
        b = self.fact[k]
        c = self.fact[n - k]
        return (
            a * self.power_func(b, self.p - 2) * self.power_func(c, self.p - 2)
        ) % self.p

    def power_func(self, a: int, b: int) -> int:
        # a^b mod p
        # O(log(b))
        ans = 1
        while b > 0:
            if b & 1:
                ans = ans * a % self.p
            a = a * a % self.p
            b >>= 1
        return ans

    def catalan(self, a: int) -> int:
        return (self.comb(a * 2, a) - self.comb(a * 2, a - 1)) % self.p


if __name__ == "__main__":
    n = int(input())
    facts = Facts(n)
    print(facts.catalan(n))