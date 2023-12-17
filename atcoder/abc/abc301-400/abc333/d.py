from collections import defaultdict, deque
n = int(input())
uv = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    uv[u].append(v)
    uv[v].append(u)

ans = float("inf")
visited = set([1])
if len(uv[1]) == 1:
    ans = 0
else:
    counts = []
    for c in uv[1]:
        visited = set([1])
        visited.add(c)
        q = deque([c])
        count = 1
        while q:
            v = q.popleft()
            for e in uv[v]:
                if e in visited:
                    continue
                visited.add(e)
                q.append(e)
                count += 1
        counts.append(count)
    counts.sort()
    ans = sum(counts[:-1])
print(ans + 1)