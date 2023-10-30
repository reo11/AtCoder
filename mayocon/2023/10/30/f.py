# 前計算で各S, Gと各お菓子の最短距離を求めておく
import time
from collections import deque
INF = float("inf")
start_at = time.time()
h, w, t = map(int, input().split())
a = [list(input()) for _ in range(h)]
# お菓子の個数をnとする
positions = []
start = ()
goal = ()
n = 0
for i in range(h):
    for j in range(w):
        if a[i][j] == "o":
            n += 1
            positions.append((i, j))
            a[i][j] = str(n)
        if a[i][j] == "S":
            start = (i, j)
        if a[i][j] == "G":
            goal = (i, j)
positions = [start] + positions + [goal]

nums = []
num_map = dict()
for i in range(2 + n):
    if i == 0:
        num_map["S"] = 0
        nums.append("S")
    elif i == 1 + n:
        num_map["G"] = 1 + n
        nums.append("G")
    else:
        num_map[str(i)] = i
        nums.append(str(i))

# 2 + n個の頂点から幅優先探索をそれぞれ行なってdistance_matrixを生成する
distance_matrix = [[INF] * (2 + n) for _ in range(2 + n)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for start_pos in range(2 + n):
    visited = [[False] * w for _ in range(h)]
    que = deque([[0, positions[start_pos]]]) # [distance, pos]
    count = 0
    while que:
        cost, pos = que.popleft()
        visited[pos[0]][pos[1]] = True
        if cost >= t:
            break
        for dy, dx in dxy:
            next_pos = (pos[0] + dy, pos[1] + dx)
        
            if next_pos[0] < 0 or next_pos[0] >= h or next_pos[1] < 0 or next_pos[1] >= w:
                continue
            if visited[next_pos[0]][next_pos[1]]:
                continue
            next_aij = a[next_pos[0]][next_pos[1]]
            if next_aij == "#":
                continue
            if next_aij in num_map:
                count += 1
                distance_matrix[start_pos][num_map[next_aij]] = cost + 1
                distance_matrix[num_map[next_aij]][start_pos] = cost + 1
            visited[next_pos[0]][next_pos[1]] = True
            que.append([cost + 1, next_pos])
        if count == n + 1:
            break

# どの頂点を訪れるかあらかじめ決めておく
# 2 * n = 2^18 = 262144
# bitDP
# dp[i][j] = 状態iで最後に頂点jにいるときの最小コスト
dp = [[INF] * (2 + n) for _ in range(1 << (n + 2))]
dp[1][0] = 0

for i in range(1 << (n + 2)):
    for j in range(2 + n):
        if dp[i][j] == INF:
            continue
        for k in range(2 + n):
            if i & (1 << k):
                continue
            dp[i | (1 << k)][k] = min(dp[i | (1 << k)][k], dp[i][j] + distance_matrix[j][k])

ans = -1
for i in range(len(dp)):
    cost = dp[i][-1]
    # print(i, cost)
    if cost <= t:
        count = 0
        for j in range(1, 1 + n):
            if i & (1 << j):
                count += 1
        ans = max(ans, count)
    # print("i:", i, "ans:", ans)        
# print(dp)
# print(distance_matrix)
print(ans)