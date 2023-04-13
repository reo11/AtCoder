import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n = int(input())
edges = defaultdict(lambda: [])
uv = []
for _ in range(n):
    u, v = map(int, input().split())
    uv.append([u, v])
    edges[u].append(v)
    edges[v].append(u)
q = int(input())
xy = []
for _ in range(q):
    x, y = map(int, input().split())
    xy.append([x, y])
ans = []

# 閉路解析？
# N頂点あるので、どこかで必ずループが発生している
# 1. 閉路を構成する頂点の集合Sを生成
# 2. Sに入っていない範囲でグループGを作成
# 3. 同じGに所属する場合: Yes, 他はNo
# 閉路は1つしかない(頂点数=辺の数なので)

# 1. dfsで閉路を見つける
# l: これまでの道のり
# 次数で特定可能
def dfs(l, current_edge_num, s):
    if len(edges[current_edge_num]) == 1:
        # 行き止まり
        return None
    for next_edge_num in edges[current_edge_num]:
        if len(l) > 0 and l[-1] == next_edge_num:
            continue
        if next_edge_num in s:
            ret_s = set()
            for edge_i in reversed(l + [current_edge_num]):
                ret_s.add(edge_i)
                if edge_i == next_edge_num:
                    break
            return ret_s
        if len(edges[next_edge_num]) <= 1:
            continue
        s_i = dfs(l + [current_edge_num], next_edge_num, s | {current_edge_num})
        if s_i:
            return s_i
    return None
loop_set = dfs([], 1, set())
if not loop_set:
    # RE対策？
    loop_set = set()

# 2. loop_setにたどり着くまでグループ分け
group_id = 0
edge_groups = defaultdict(lambda: -1)
group_members = defaultdict(lambda: set())

for i in range(1, n + 1):
    if edge_groups[i] != -1:
        # 所属済み
        continue

    current_edge = i
    q = [current_edge]
    while len(q) > 0:
        current_edge = q.pop()
        if edge_groups[current_edge] != -1:
            continue
        # 次の頂点もグループに入れる
        edge_groups[current_edge] = group_id
        group_members[group_id].add(current_edge)
        for next_edge in edges[current_edge]:
            if current_edge in loop_set and next_edge in loop_set:
                continue
            if edge_groups[next_edge] != -1:
                continue
            q.append(next_edge)
    group_id += 1

for x, y in xy:
    if edge_groups[x] != edge_groups[y]:
        ans.append("No")
    else:
        ans.append("Yes")

print("\n".join(ans))