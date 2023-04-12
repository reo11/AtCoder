INF = float('inf')
h, w, c = map(int, input().split())
arr = []
r_arr = []
for _ in range(h):
    l = list(map(int, input().split()))
    arr.append(l)
    r_arr.append(list(reversed(l)))

def solve(a):
    dp = [[INF for _ in range(w + 1)] for _ in range(h + 1)]
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            dp[i][j] = min(a[i - 1][j - 1], dp[i - 1][j] + c, dp[i][j - 1] + c)

    ans = INF
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            ans = min(ans, dp[i - 1][j] + c + a[i - 1][j - 1])
            ans = min(ans, dp[i][j - 1] + c + a[i - 1][j - 1])
    return ans

print(min(solve(arr), solve(r_arr)))