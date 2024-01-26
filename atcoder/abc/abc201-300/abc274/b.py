h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]
ans = [0 for _ in range(w)]

for i in range(h):
    for j in range(w):
        if c[i][j] == "#":
            ans[j] += 1
print(*ans, sep=" ")
