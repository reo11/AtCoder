h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

# 全探索

ans = 0
for direction in [0, 1]:
    # 0: 横方向, 1: 縦方向
    for i in range(h):
        for j in range(w):
            if direction == 0 and j >= w - 1:
                continue
            if direction == 1 and i >= h - 1:
                continue
            if direction == 0:
                if s[i][j] == "." and s[i][j + 1] == ".":
                    ans += 1
            if direction == 1:
                if s[i][j] == "." and s[i + 1][j] == ".":
                    ans += 1
print(ans)
