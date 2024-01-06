import sys
from collections import defaultdict, deque
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)
INF = float("inf")

n, m = map(int, input().split())
a = list(map(int, input().split()))
uv = []
paths = defaultdict(lambda: [])
for _ in range(m):
    u, v = map(int, input().split())
    if a[u - 1] <= a[v - 1]:
        paths[u].append(v)
    if a[v - 1] <= a[u - 1]:
        paths[v].append(u)

# 各頂点にそこにいくまでの最高得点を記録していく
scores = defaultdict(lambda: -INF)
q = [(1, 1, 0)]
visited_path = set()
path = []

while q:
    current_node_num, current_score, depth = q.pop()
    while len(path) > depth:
        visited_path.discard(path.pop())
    if scores[current_node_num] > current_score:
        # もっと良い手順がある
        continue
    if current_node_num == n:
        continue
    value = a[current_node_num - 1]
    for next_node_num in paths[current_node_num]:
        if next_node_num in visited_path:
            continue
        next_score = current_score
        if value != a[next_node_num - 1]:
            next_score += 1
        if scores[next_node_num] >= next_score:
            continue

        q.append((next_node_num, next_score, depth + 1))
        scores[next_node_num] = max(scores[next_node_num], next_score)

if scores[n] == -INF:
    print(0)
else:
    print(scores[n])
