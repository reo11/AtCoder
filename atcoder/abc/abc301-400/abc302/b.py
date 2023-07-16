h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
target = list("snuke")
dxy = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]

for i in range(h):
    for j in range(w):
        if target[0] == s[i][j]:
            for dx, dy in dxy:
                flag = True
                ans = [f"{i + 1} {j + 1}"]
                for k in range(1, 5):
                    if i + k * dy < 0 or i + k * dy >= h:
                        flag = False
                        break
                    if j + k * dx < 0 or j + k * dx >= w:
                        flag = False
                        break
                    if target[k] == s[i + k * dy][j + k * dx]:
                        ans.append(f"{i + k * dy + 1} {j + k * dx + 1}")
                    else:
                        flag = False
                        break
                if flag:
                    print(*ans, sep="\n")
                    exit()
