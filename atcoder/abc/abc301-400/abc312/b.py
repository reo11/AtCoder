n, m = map(int, input().split())
s = [list(input()) for _ in range(n)]

ans = []
for i in range(n - 8):
    for j in range(m - 8):
        # 全探索する
        # #が左上に3x3で存在して、右下にも3x3で存在しているかを確認する
        left_up_white = 0
        left_up = 0
        for ii in range(4):
            for jj in range(4):
                if ii == 3 or jj == 3:
                    if s[i + ii][j + jj] == ".":
                        left_up_white += 1
                elif 0 <= i+ii < n and 0 <= j+jj < m:
                    if s[i+ii][j+jj] == "#":
                        left_up += 1
        right_down_white = 0
        right_down = 0
        for ii in range(4):
            for jj in range(4):
                if ii == 0 or jj == 0:
                    if s[i + 5 + ii][j + 5 + jj] == ".":
                        right_down_white += 1
                elif 0 <= i + 5 + ii < n and 0 <= j + 5 + jj < m:
                    if s[i + 5 + ii][j + 5 + jj] == "#":
                        right_down += 1
        # print(left_up_white, left_up, right_down_white, right_down)
        if left_up_white == 7 and left_up == 9 and right_down_white == 7 and right_down == 9:
            ans.append(f"{i + 1} {j + 1}")
print(*ans, sep="\n")