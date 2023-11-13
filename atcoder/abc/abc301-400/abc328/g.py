from collections import defaultdict, deque
INF = float("inf")

n, c = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def cost_k(a):
    cost = 0
    for i in range(n):
        cost += abs(a[i] - b[i])
    return cost

# dp[i][j]: 集合iを使ってjが最後の時の最小コスト
dp = defaultdict(lambda: defaultdict(lambda: INF))
# dp = [[INF] * n for _ in range(2**n)]
## 初期化
queue = deque([])
dp[0][0] = 0
for next_num in range(n):
    dp[1 << next_num][next_num] = abs(b[0] - a[next_num])
## ここまで初期化

# もらうDP
ans = cost_k(a)
for si in range(2**n):
    bit_count = sum([1 for i in range(n) if si & (1 << i)])
    for last_num in dp[si].keys():
        if dp[si][last_num] >= ans:
            continue
        for next_num in range(n):
            if si & (1 << next_num):
                continue
            next_si = si | 1 << next_num
            if next_num == last_num + 1:
                dp[next_si][next_num] = min(dp[next_si][next_num], dp[si][last_num] + abs(b[bit_count] - a[next_num]))
            else:
                dp[next_si][next_num] = min(dp[next_si][next_num], dp[si][last_num] + abs(b[bit_count] - a[next_num]) + c)

for i in range(n):
    ans = min(ans, dp[2**n - 1][i])

print(ans)