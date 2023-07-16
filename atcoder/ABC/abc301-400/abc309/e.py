import sys
from collections import defaultdict, deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
p = list(map(int, input().split()))
xy = []

for _ in [0] * m:
    x, y = map(int, input().split())
    xy.append((x, y))

# 最大保険期間を持ちながら子孫に深さ優先探索をする

# 各人が持つ最大保険期間をdictで持つ
hoken = defaultdict(lambda: 0)
for x, y in xy:
    hoken[x] = max(hoken[x], y + 1)
# 自分の子孫の情報をdictで持つ
children = defaultdict(lambda: [])
for i, p_i in enumerate(p, start=2):
    children[p_i].append(i)

# dfs with queue
is_hoken = defaultdict(lambda: False)
q = deque([[1, hoken[1]]])
visited = defaultdict(lambda: False)

while q:
    # print(q)
    person_i, hoken_value = q.popleft()
    visited[person_i] = True
    if hoken_value > 0:
        # 保険に入っている
        is_hoken[person_i] = True
    # 子孫の分の処理を積む
    for child in children[person_i]:
        if visited[child]:
            continue
        q.append([child, max(hoken[child], hoken_value - 1)])
# print(hoken)
# print(is_hoken)
ans = 0
for i in range(1, n + 1):
    if is_hoken[i]:
        ans += 1

print(ans)
