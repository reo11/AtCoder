import sys
from functools import lru_cache

import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n = int(input())


@lru_cache(maxsize=None)
def f(k):
    if k == 0:
        return 1
    else:
        return f(k // 2) + f(k // 3)


print(f(n))
