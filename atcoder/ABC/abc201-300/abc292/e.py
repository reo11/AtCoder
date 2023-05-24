from collections import defaultdict, deque

# unionfind木でグループ分け
# 各頂点が所属するグループ内の他の頂点に対して全探索
# O(NM) # 4 * 10 ^ 6
n, m = map(int, input().split())
uv = []

# 有向辺
edges = defaultdict(lambda: set())

for _ in range(m):
    u, v = map(int, input().split())
    edges[u].add(v)

ans = 0
for current_edge in range(1, n + 1):
    # 到達可能な頂点数を調べる
    subq = deque([current_edge])
    checked = set([current_edge])
    edges_to_add = []
    while len(subq) > 0:
        c = subq.popleft()
        for next_edge in edges[c]:
            if next_edge == current_edge:
                continue
            if next_edge not in checked:
                checked.add(next_edge)
                subq.append(next_edge)
    ans += len(checked - edges[current_edge] - {current_edge})
print(ans)
