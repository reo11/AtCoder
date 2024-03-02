from collections import defaultdict, deque
import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)
INF = float("inf")

n, m = map(int, input().split())
to_path = defaultdict(lambda: [])
for _ in range(m):
    l, d, k, c, a, b = map(int, input().split())
    to_path[b].append((l, d, k, c, a, b))

def calc_max_ts(l, d, k, c, a, b, ts):
    # ts: 駅bに到着しているべき時刻
    # return: 駅aに到着している時刻
    if ts < l + c:
        # 終電に間に合う電車が存在しない
        return -INF
    elif ts >= l + (k - 1) * d + c:
        # 最も遅い電車で良い
        return l + (k - 1) * d
    else:
        # 適切なkを探す必要がある
        ki = (l + (k - 1) * d + c) - ts
        if ki % d == 0:
            ki //= d
        else:
            ki = ki // d + 1
        return l + (k - 1 - ki) * d

# Nから逆に辿っていく
# その駅の終電時刻: max_ts
max_ts = defaultdict(lambda: -INF)
q = []
heapq.heapify(q)
for l, d, k, c, a, b in to_path[n]:
    max_ts[b] = max(max_ts[b], l + (k - 1) * d + c)
heapq.heappush(q, [-max_ts[b], b])

visited = set([])
while q:
    current_station = heapq.heappop(q)[1]
    if current_station in visited:
        continue
    visited.add(current_station)
    for l, d, k, c, a, b in to_path[current_station]:
        # 選択肢の中から最も遅い電車を選択する
        tsi = calc_max_ts(l, d, k, c, a, b, max_ts[b])
        max_ts[a] = max(max_ts[a], tsi)
        if a not in visited and max_ts[a] != -INF:
            heapq.heappush(q, [-max_ts[a], a])

ans = []
for i in range(1, n):
    if max_ts[i] == -INF:
        ans.append("Unreachable")
    else:
        ans.append(max_ts[i])
print(*ans, sep="\n")
