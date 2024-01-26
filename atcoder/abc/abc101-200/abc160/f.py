# 全方位DP
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import defaultdict, deque
from math import factorial

MOD = 10**9 + 7


class Facts:
    def __init__(self, max_num=10**5, p=10**9 + 7):
        self.p = p
        self.max_num = max_num
        self.fact = [1] * (self.max_num + 1)
        for i in range(1, self.max_num + 1):
            self.fact[i] = self.fact[i - 1] * i
            self.fact[i] %= self.p

    def power_func(self, a, b):
        ans = 1
        while b > 0:
            if b & 1:
                ans = ans * a % self.p
            a = a * a % self.p
            b >>= 1
        return ans

    def fact_inv(self, a):
        return self.power_func(a, self.p - 2) % self.p


n = int(input())
fact = Facts(max_num=200000)
edges = defaultdict(lambda: [])

for _ in range(n - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

# step1 吸い上げ
size = [1 for _ in range(n + 1)]


def dfs1(num, par=-1):
    res = 1
    for node in edges[num]:
        if node == par:
            continue
        else:
            res += dfs1(node, num)
    res %= MOD
    size[num] = res
    return res


dfs1(1)
# print(size)
dp = [0 for _ in range(n + 1)]


def dfs2(n, par=-1):
    res = fact.fact[size[n] - 1]
    for node in edges[n]:
        if node == par:
            continue
        else:
            res *= dfs2(node, n) * fact.fact_inv(fact.fact[size[node]])
    res %= MOD
    dp[n] = res
    return res


dfs2(1)
# print(dp)

# step2 還元
ans = [0 for _ in range(n + 1)]
inv_1 = fact.fact_inv(fact.fact[n - 1])


def dfs3(num, par=-1):
    if par != -1:
        res = (
            dp[num]
            * fact.fact_inv(fact.fact[size[num] - 1])
            * fact.fact[n - 1]
            * ans[par]
            * inv_1
            * fact.fact[n - size[num] - 1]
            * fact.fact[size[num]]
            * fact.fact_inv(dp[num])
            * fact.fact_inv(fact.fact[n - size[num]])
            % MOD
        )
        ans[num] = res
    else:
        ans[num] = dp[num]
    for node in edges[num]:
        if node == par:
            continue
        dfs3(node, num)


dfs3(1)
print("\n".join(list(map(str, ans[1:]))))
