import sys
input = lambda: sys.stdin.readline().rstrip()

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

l = []
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            l.append([i, j])

bb = [100000, 0, 100000, 0]
for y, x in l:
    bb[0] = min(bb[0], y)
    bb[1] = max(bb[1], y)
    bb[2] = min(bb[2], x)
    bb[3] = max(bb[3], x)
# print(bb)

ans = [-1, -1]

for i in range(bb[0], bb[1]+1):
    for j in range(bb[2], bb[3]+1):
        if s[i][j] == ".":
            ans = [i, j]
            break
    else:
        continue
    break
print(f"{ans[0] + 1} {ans[1] + 1}")