from collections import defaultdict
MOD = 998244353

a, b = map(int, input().split())
if b == 0:
    print(0)
    exit()
# a**bの正の約数の総積はaで何回割り切れるか

def prime_factorize(n):
    # 素因数分解
    # Return list of prime factorized result
    # O(sqrt(n))
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if i == n:
            continue
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                if n // i == n:
                    continue
                divisors.append(n // i)
    divisors.append(n)
    divisors.sort()
    return divisors

class FLT:
    """
    フェルマーの小定理
    a^(-1) = a^(m-2) mod p
    """

    def __init__(self, mod: int = 10 ** 9 + 7) -> None:
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

a_primes = prime_factorize(a)
prime_counter = defaultdict(int)
for ai in a_primes:
    prime_counter[ai] += 1

ans = 0
# aを素因数分解した時に含まれる最も頻度が少ない素数がネックとなる
counter = defaultdict(int)
for api in a_primes:
    counter[api] += 1
target_num = sorted(counter.items(), key=lambda x: x[1])[0][0]
# 約数の中からtarget_numの倍数と生成される数を数える
minus = 1
ans = 1
for num, value in counter.items():
    if num != target_num:
        ans *= value * b + 1  # 1のケースもあるので+1
        ans %= MOD
        minus *= value * b + 1
        minus %= counter[target_num]
ans *= b * (b + 1) // 2
minus *= b * (b + 1) // 2
minus %= counter[target_num]
# これだとtarget_numの個数で、target_numがaに2個以上含まれる場合を考慮できていない
print((ans - minus) % MOD)