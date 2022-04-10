from collections import defaultdict
from typing import Dict
import sys
import queue


input = sys.stdin.readline
INF = 10 ** 12

n = int(input())
edges = defaultdict(lambda: [])
for _ in range(n - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

max_dist = [0, -1]
min_route: Dict[int, int] = defaultdict(lambda: INF)
min_route[1] = 0

# 適当な場所から一番遠いところを探す
visited_set = set()
q = queue.Queue()
q.put((1, 0))
while not q.empty():
    edge_num, dist = q.get()
    visited_set.add(edge_num)
    for next_edge in edges[edge_num]:
        if next_edge in visited_set:
            continue
        if dist + 1 < min_route[next_edge]:
            min_route[next_edge] = dist + 1
            if max_dist[1] < dist + 1:
                max_dist[0] = next_edge
                max_dist[1] = dist + 1
            q.put((next_edge, dist + 1))

# 一番遠いところから一番遠いところを探す=直径
max_dist_v2 = [0, -1]
min_route: Dict[int, int] = defaultdict(lambda: INF)
min_route[max_dist[0]] = 0
visited_set = set()
q = queue.Queue()
q.put((max_dist[0], 0))
while not q.empty():
    edge_num, dist = q.get()
    visited_set.add(edge_num)
    for next_edge in edges[edge_num]:
        if next_edge in visited_set:
            continue
        if dist + 1 < min_route[next_edge]:
            min_route[next_edge] = dist + 1
            if max_dist_v2[1] < dist + 1:
                max_dist_v2[0] = next_edge
                max_dist_v2[1] = dist + 1
            q.put((next_edge, dist + 1))

# 直径 + 頂点を行き来する1本
print(max_dist_v2[1] + 1)
