from collections import defaultdict
n, q = map(int, input().split())
q = [list(map(int, input().split())) for _ in range(q)]
edges = defaultdict(lambda: set())
ans = []
count = n
for query in q:
    if query[0] == 1:
        u = query[1]
        v = query[2]
        if len(edges[u]) == 0:
            count -= 1
        if len(edges[v]) == 0:
            count -= 1
        edges[u].add(v)
        edges[v].add(u)
    else:
        u = query[1]
        other = edges[u]
        for i in other:
            edges[i].discard(u)
            if len(edges[i]) == 0:
                count += 1
        if len(edges[u]) > 0:
            count += 1
        edges[u] = set()
    ans.append(count)
print(*ans, sep="\n")