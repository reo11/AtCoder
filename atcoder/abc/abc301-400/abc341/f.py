from collections import defaultdict, deque

n, m = map(int, input().split())
uv = []
for _ in range(m):
    u, v = map(int, input().split())
    uv.append((u, v))
w = list(map(int, input().split()))
a = list(map(int, input().split()))
max_w = max(w)

edges = defaultdict(list)
for i, (u, v) in enumerate(uv):
    uw = w[u - 1]
    vw = w[v - 1]
    if uw > vw:
        edges[u].append(v)
    elif uw < vw:
        edges[v].append(u)

# 末端からそれぞれのポテンシャルを評価する
queue = []
for i in range(n):
    queue.append((w[i], i + 1))
queue.sort()
queue = deque(queue)

dp = [[1 for _ in range(max_w + 1)] for _ in range(n + 1)]
while queue:
    wi, i = queue.popleft()
    for j in edges[i]:
        wj = w[j - 1]
        for k in reversed(range(max_w - wj + 1)):
            dp[i][k + wj] = max(dp[i][k + wj], dp[i][k] + dp[j][wj - 1])
ans = 0
for i, ai in enumerate(a):
    if ai == 0:
        continue
    ans += dp[i + 1][w[i] - 1] * ai
print(ans)