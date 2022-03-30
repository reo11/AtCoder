from collections import deque, defaultdict
n, x, y = map(int, input().split())

edges = defaultdict(lambda: [])
for i in range(1, n):
    edges[i].append(i+1)
    edges[i+1].append(i)
edges[x].append(y)
edges[y].append(x)

# 幅優先
counter = [0 for i in range(n)]
for i in range(1, n+1):
    d = deque()
    is_checked = [False for _ in range(n+1)]
    dist = [-1 for _ in range(n+1)]
    dist[i] = 0
    d.append((i, 0))
    while len(d) > 0:
        e, pre_dist = d.popleft()
        if is_checked[e]:
            continue
        else:
            is_checked[e] = True
            dist[e] = pre_dist + 1
            for next_e in edges[e]:
                if not is_checked[next_e]:
                    d.append((next_e, pre_dist+1))
    for j in range(i+1, n+1):
        counter[dist[j]-1] += 1
print("\n".join(list(map(str, counter[1:]))))
