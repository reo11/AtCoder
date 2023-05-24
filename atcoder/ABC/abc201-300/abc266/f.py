import sys
from collections import defaultdict, deque

input = sys.stdin.readline

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
q = deque()
q.append([-1, 1])
l = deque()
s = set()
loop_set = set()
while len(q) > 0:
    pre, current_edge_num = q.popleft()
    l.append(current_edge_num)
    s.add(current_edge_num)

    if len(l) > 1 and len(edges[current_edge_num]) == 1:
        # 行き止まりの場合、q[0]の値になるまで戻る
        while True:
            if l[-1] == q[0][0]:
                break
            else:
                l.pop()
        continue

    for next_edge_num in edges[current_edge_num]:
        if len(l) > 1 and l[-2] == next_edge_num:
            continue
        if next_edge_num in s:
            for edge_i in reversed(l):
                loop_set.add(edge_i)
                if edge_i == next_edge_num:
                    break
            q = deque()
            break
        q.appendleft([current_edge_num, next_edge_num])

# 2. loop_setにたどり着くまでグループ分け
edge_groups = [-1 for _ in range(n + 1)]
group_members = [set() for _ in range(n + 1)]

q = deque()
for i in range(1, n + 1):
    q.append([i, i])

while len(q) > 0:
    current_edge, current_group_id = q.popleft()
    if edge_groups[current_edge] != -1:
        continue
    # 次の頂点もグループに入れる
    edge_groups[current_edge] = current_group_id
    group_members[current_group_id].add(current_edge)
    for next_edge in edges[current_edge]:
        if current_edge in loop_set and next_edge in loop_set:
            continue
        if edge_groups[next_edge] != -1:
            continue
        q.appendleft([next_edge, current_group_id])

# print(loop_set)
# print(edge_groups)
# print(group_members)

for x, y in xy:
    if edge_groups[x] != edge_groups[y]:
        ans.append("No")
    else:
        ans.append("Yes")

print("\n".join(ans))
