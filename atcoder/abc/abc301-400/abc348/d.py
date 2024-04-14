from collections import defaultdict
from heapq import heappop, heappush, heapify

h, w = map(int, input().split())
a = [[i for i in list(str(input()))] for _ in range(h)]
n = int(input())
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

rce = [[0] * w for _ in range(h)]
visited = defaultdict(lambda: False)
def fmt_visted_key(r, c, nr, nc):
    return f"{r}_{c}_{nr}_{nc}"

for i in range(n):
    r, c, e = map(int, input().split())
    rce[r - 1][c - 1] = e

q = []
heapify(q)

start = [0, 0]
for i in range(h):
    for j in range(w):
        if a[i][j] == "S":
            heappush(q, (-rce[i][j], i, j, -1, -1))
            for dx, dy in dxy:
                pr, pc = i - dx, j - dy
                if pr < 0 or pr >= h:
                    continue
                if pc < 0 or pc >= w:
                    continue
                if a[pr][pc] == "#":
                    continue
                visited[fmt_visted_key(pr, pc, i, j)] = True

while q:
    e, r, c, pr, pc = heappop(q)
    e = -e
    if visited[fmt_visted_key(pr, pc, r, c)]:
        continue
    visited[fmt_visted_key(pr, pc, r, c)] = True

    if e <= 0:
        continue

    for dx, dy in dxy:
        nr, nc = r + dx, c + dy
        if nr < 0 or nr >= h:
            continue
        if nc < 0 or nc >= w:
            continue
        if a[nr][nc] == "#":
            continue
        if rce[nr][nc] >= e - 1 and visited[fmt_visted_key(r, c, nr, nc)]:
            continue

        v = max(rce[nr][nc], e - 1)
        rce[nr][nc] = v

        if e > 0 and a[nr][nc] == "T":
            print("Yes")
            exit()

        heappush(q, (-v, nr, nc, r, c))

print("No")
