import sys
from collections import defaultdict, deque
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
edges = defaultdict(lambda: [])
for a, b in ab:
    edges[a].append(b)
    edges[b].append(a)
c = list(map(int, input().split()))

# dpっぽいことをする
# i頂点目に0/1の状態から出発できたかどうかをそれぞれ保持しながら探索を行う
# 探索数は最大でO(2 * M) = O(M)程度

dp = [[[False for _ in range(2)] for _ in range(2)] for _ in range(n + 1)]
dp[1][c[0]][0] = True # 頂点1をc[0]で初期化
dp[1][c[0]][1] = True # 頂点1をc[0]で初期化

for i in range(1, n + 1):
    dp[i][c[i - 1]][0] = True

q = deque([])
q.append([1, c[0]])

while q:
    now, color = q.popleft()
    dp[now][color][1] = True
    if color == 0:
        next_color = 1
    else:
        next_color = 0

    count = 0
    for next in edges[now]:
        if dp[next][next_color][1] == False and dp[next][next_color][0]:
            dp[next][next_color][1] = True
            q.append([next, next_color])
            count += 1
    if count > 0:
        dp[now][next_color][0] = True

if c[0] == 0:
    finish_color = 1
else:
    finish_color = 0

if dp[1][finish_color][1]:
    print("Yes")
else:
    print("No")