import sys
import pypyjit
from functools import lru_cache
pypyjit.set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n = int(input())

@lru_cache(maxsize=None)
def func_s(i):
    if i == 1:
        return [1]
    else:
        return func_s(i-1) + [i] + func_s(i-1)

print(*func_s(n), sep=" ")