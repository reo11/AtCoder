h, w, k = map(int, input().split())
a = [list(input()) for i in range(h)]

ans = [[0 for _ in range(w)] for _ in range(h)]
count = 1
points = []
for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            ans[i][j] = count
            points.append((i, j))
            count += 1

def dfs(i, j):
    global ans
    ans

