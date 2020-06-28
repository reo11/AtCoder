from collections import defaultdict

class LCM_mod:
    """
    最小公倍数の計算を行う
    オーバーフローが発生しないように素因数分解し,
    因数の積を逐次余りに置き換えて最小公倍数を導出する.
    """
    def __init__(self, max_num, p=10**9+7):
        self.max_num = max_num + 1
        self.p = p
        self.prime = [0 for _ in range(self.max_num)]
        self.max_map = defaultdict(int)
        self.sieve()

    def rep_sqr(self, base, k):
        # 繰り返し二乗法
        if k == 0:
            return 1
        elif k % 2 == 0:
            return (self.rep_sqr(base, k / 2) ** 2) % self.p
        else:
            return (self.rep_sqr(base, k - 1) * base) % self.p

    def sieve(self):
        """
        エラトステネスの篩　O(n)
        nまでに含まれる素数を導出
        """
        self.prime[0], self.prime[1] = 1, 1
        for i in range(2, self.max_num):
            if self.prime[i] == 0:
                for j in range(i * 2, self.max_num, i):
                    if self.prime[j] == 0:
                        self.prime[j] = i
                self.prime[i] = i

    def lcm_list_mod(self, arr):
        """
        listのそれぞれの要素について、素因数分解する
        それぞれの因数について最大であれば更新する
        """
        for i in range(len(arr)):
            num = arr[i]
            d = defaultdict(int)

            while num > 1:
                fact = self.prime[num]
                d[fact] += 1
                num //= fact

            for i in d.keys():
                self.max_map[i] = max(self.max_map[i], d[i])

        ans = 1
        for i in self.max_map.keys():
            ans = (ans * self.rep_sqr(i, self.max_map[i])) % self.p
        return ans


class FLT:
    def __init__(self, mod=10**9+7):
        self.mod = mod

    def rep_sqr(self, base, k):
        if k == 0:
            return 1
        elif k % 2 == 0:
            return (self.rep_sqr(base, k // 2) ** 2) % self.mod
        else:
            return (self.rep_sqr(base, k - 1) * base) % self.mod

    def inv(self, a):
        """ 逆元を取る """
        return self.rep_sqr(a, self.mod-2)

n = int(input())
a = list(map(int, input().split()))
MOD = 10**9+7

lcm_mod = LCM_mod(max(a), MOD)
lcm_all = lcm_mod.lcm_list_mod(a)
flt = FLT(MOD)

b = list(map(lambda x: lcm_all * flt.inv(x), a))
ans = 0
for i in range(len(b)):
    ans += b[i]
    ans %= MOD
print(ans)
