import sys
from itertools import product

input = lambda: sys.stdin.readline().rstrip()

h, w, k = map(int, input().split())
c = [[i for i in list(str(input()))] for i in range(h)]


def check(sh, sw):
    cnt = 0
    for i in range(h):
        if sh[i]:
            continue
        for j in range(w):
            if sw[j]:
                continue
            if c[i][j] == "#":
                cnt += 1
    return cnt


ans = 0
for p1 in product(range(2), repeat=w):
    for p2 in product(range(2), repeat=h):
        if check(p2, p1) == k:
            ans += 1
print(ans)
