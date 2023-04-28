from collections import defaultdict, deque
n, m = map(int, input().split())
edges = defaultdict(lambda: [])

for _ in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

count_edge = 0
for i in range(1, n + 1):
    if len(edges[i]) > 2 or len(edges[i]) == 0:
        print("No")
        exit()
    if len(edges[i]) == 1:
        count_edge += 1
if count_edge != 2:
    print("No")
    exit()

q = deque()
q.append(1)
checked = defaultdict(lambda: False)

count = 0
while len(q) > 0:
    node = q.popleft()
    if checked[node]:
        continue
    checked[node] = True
    count += 1

    for node_i in edges[node]:
        if checked[node_i]:
            continue
        q.append(node_i)

if count == n:
    print("Yes")
else:
    print("No")