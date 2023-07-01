import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

h, w = map(int, input().split())
s = []
for _ in range(h):
    s_i = list(input())
    s.append(s_i)

# 深さ優先探索で探す
snuke = ["s", "n", "u", "k", "e"]
dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[False] * w for _ in range(h)]
def dfs(x, y, step = 0):
    if snuke[(step % 5)] != s[y][x]:
        return False
    # print(x, y, step)
    visited[y][x] = True
    # 4方向に探索
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if 0 <= ny < h and 0 <= nx < w:
            if visited[ny][nx]:
                continue
            if s[ny][nx] == snuke[((step + 1) % 5)]:
                if nx == w - 1 and ny == h - 1:
                    return True
                if dfs(nx, ny, step + 1):
                    return True
            else:
                continue
        else:
            continue
    return False
if dfs(0, 0):
    print("Yes")
else:
    print("No")