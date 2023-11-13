from collections import defaultdict
n, m = map(int, input().split())
ab = []
path = defaultdict(lambda: [])
for _ in range(m):
    a, b = map(int, input().split())
    ab.append((a, b))
    path[a].append(b)
    path[b].append(a)

ans = []
for i in range(1, n + 1):
    ansi = []
    for j in path[i]:
        ansi.append(j)
    ansi = sorted(ansi)
    ans.append(f"{len(ansi)} {' '.join(list(map(str, ansi)))}")
print("\n".join(ans))
