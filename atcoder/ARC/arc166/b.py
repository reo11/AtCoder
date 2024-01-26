import itertools
import sys
from collections import defaultdict
from functools import lru_cache

import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)


@lru_cache(maxsize=None)
def gcd(a: int, b: int) -> int:
    # 最大公約数
    # (12, 18) -> 6
    while b:
        a, b = b, a % b
    return a


@lru_cache(maxsize=None)
def lcm(x: int, y: int) -> int:
    # 最小公倍数
    # (12, 18) -> 36
    return (x * y) // gcd(x, y)


INF = float("inf")
n, a, b, c = map(int, input().split())
A = list(map(int, input().split()))
abc = [a, b, c]

# 割り当て優先度を全探索する
# 3 * 2 * 1 = 6通り

# print(perm)
patterns = [["a", "b", "c"], ["ab", "c"], ["ac", "b"], ["bc", "a"], ["abc"]]
mod_abc = defaultdict(lambda: [])

ab = lcm(a, b)
bc = lcm(b, c)
ac = lcm(a, c)
abc = lcm(ab, c)
for i in range(n):
    ai = A[i]
    mod_abc["a"].append([a - (ai % a), i])
    mod_abc["b"].append([b - (ai % b), i])
    mod_abc["c"].append([c - (ai % c), i])
    mod_abc["ab"].append([ab - (ai % ab), i])
    mod_abc["ac"].append([ac - (ai % ac), i])
    mod_abc["bc"].append([bc - (ai % bc), i])
    mod_abc["abc"].append([abc - (ai % abc), i])

for k in mod_abc.keys():
    mod_abc[k] = sorted(mod_abc[k], key=lambda x: x[0])[:3]

ans = INF
for pattern_orders in patterns:
    if n < len(pattern_orders):
        continue
    candidate = []
    for pattern_i in pattern_orders:
        candidate.append(mod_abc[pattern_i][: len(pattern_orders)])
    for candidatei in itertools.product(*candidate):
        used_i = set()
        cost = 0
        flag = True
        for costi, i in candidatei:
            if i in used_i:
                flag = False
                break
            cost += costi
            used_i.add(i)

        if flag:
            ans = min(ans, cost)

print(ans)
