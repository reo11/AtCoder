import heapq
from collections import defaultdict

n, m = map(int, input().split())
edges = defaultdict(lambda: defaultdict(lambda: float("inf")))
abc = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a][b] = c
    edges[b][a] = c

# 街iと街jの最短距離を前計算できれば1-k + k-Nのコストを計算し続けてO(N)で求まる
# 無向グラフなので、1から各k及びNから各kを計算できれば良い
# ダイクストラを2回回せばO(N + M)で解ける
# O(N + M) + O(N)

# ダイクストラ
q = [[0, 1]]
heapq.heapify(q)
dist_from_1 = defaultdict(lambda: float("inf"))
# 街1から

while q and len(dist_from_1) < n:
    # ダイクストラなので、popした瞬間に最適が確定する
    cost, current_num = heapq.heappop(q)
    if current_num in dist_from_1:
            continue
    dist_from_1[current_num] = cost

    for next_num in edges[current_num].keys():
        heapq.heappush(q, [cost + edges[current_num][next_num], next_num])

q = [[0, n]]
heapq.heapify(q)
dist_from_n = defaultdict(lambda: float("inf"))
# 街1から

while q and len(dist_from_n) < n:
    # ダイクストラなので、popした瞬間に最適が確定する
    cost, current_num = heapq.heappop(q)
    if current_num in dist_from_n:
        continue
    dist_from_n[current_num] = cost

    for next_num in edges[current_num].keys():
        heapq.heappush(q, [cost + edges[current_num][next_num], next_num])

ans = []
for i in range(1, n + 1):
    ans.append(str(dist_from_1[i] + dist_from_n[i]))
# print(dist_from_1)
# print(dist_from_n)
# print(ans)
print(*ans, sep="\n")
