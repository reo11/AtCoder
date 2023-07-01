import sys

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)


def solve(n, p):
    ans = 0
    for i, p_i in enumerate(p, start=1):
        if p_i - i >= 0:
            ans += 1
    return ans


ans = []
t = int(input())
for _ in [0] * t:
    n = int(input())
    p = list(map(int, input().split()))
    ans.append(solve(n, p))
print(*ans, sep="\n")
