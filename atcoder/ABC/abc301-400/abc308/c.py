import sys
from decimal import Decimal
input = lambda: sys.stdin.readline().rstrip()

def solve1(ab):
    ans = []
    for i, (a, b) in enumerate(ab, start=1):
        p = (10**20 * a) // (a + b)
        ans.append([p, i])
    ans.sort(key=lambda x: (-x[0], x[1]))
    ans = [i for _, i in ans]
    return ans

def solve2(ab):
    ans = []
    for i, (a, b) in enumerate(ab, start=1):
        p = Decimal(a) / Decimal(a + b)
        ans.append([p, i])
    ans.sort(key=lambda x: (-x[0], x[1]))
    ans = [i for _, i in ans]
    return ans

n = int(input())
ab = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append([a, b])
print(*solve2(ab), sep=' ')
