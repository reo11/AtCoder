# 角の数を数える

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

ans = 0
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dxy2 = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
for i in range(1, h - 1):
    for j in range(1, w - 1):
        if s[i][j] == ".":
            continue
        cnt = 0
        for k in range(4):
            x, y = dxy[k]
            if s[i + x][j + y] == ".":
                cnt += 1
        cnt2 = 0
        if cnt == 1:
            continue
        elif cnt == 2:
            ans += 1
        elif cnt == 3:
            ans += 1

print(ans)
