import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
MOD = 10**9+7
h, w = map(int, input().split())
a = [[int(i) for i in input().rstrip().split()] for i in range(h)]
dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
dp = [[-1 for _ in range(w)] for _ in range(h)]

def f(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    ret = 1
    cur_num = a[i][j]
    for dx, dy in dxy:
        if 0 <= i+dx <= h-1 and 0 <= j+dy <= w-1:
            if cur_num < a[i+dx][j+dy]:
                ret += f(i+dx, j+dy)
    ret %= MOD
    dp[i][j] = ret
    return ret

ans = 0
for i in range(h):
    for j in range(w):
        ans += f(i, j)
print(ans%MOD)