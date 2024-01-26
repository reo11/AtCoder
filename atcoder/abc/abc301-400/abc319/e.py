import sys
from functools import lru_cache

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n, x, y = map(int, input().split())
pt = []
for _ in range(n - 1):
    p, t = map(int, input().split())
    pt.append((p, t))
q = int(input())
q_list = [int(input()) for _ in range(q)]

CONST_VALUE = 3 * 5 * 7 * 8
ans = []


@lru_cache(maxsize=None)
def calc_bus(time):
    start_time = time
    for p, t in pt:
        if time % p == 0:
            time += t
        else:
            time += p - (time % p)
            time += t
    return time - start_time


for qi in q_list:
    start_time = qi + x
    end_time = start_time + calc_bus(start_time % CONST_VALUE)
    ans.append(end_time + y)
print(*ans, sep="\n")
