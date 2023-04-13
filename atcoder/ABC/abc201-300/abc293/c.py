h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

def dfs(l, x, y):
    if x == w - 1 and y == h - 1:
        s = set(l)
        if len(l) == len(s):
            return 1
        else:
            return 0
    else:
        score = 0
        if x < w - 1:
            score += dfs(l + [a[y][x+1]], x + 1, y)
        if y < h - 1:
            score += dfs(l + [a[y+1][x]], x, y + 1)
        return score

print(dfs([a[0][0]], 0, 0))
