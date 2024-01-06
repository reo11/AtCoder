n = int(input())

# 外側から埋めるうずまき
# 中央はT
ans = [[0 for _ in range(n)] for _ in range(n)]
ans[0][0] = 1
ans[n // 2][n // 2] = "T"
current_pos = [1, 0]
current_num = 2
status = 0
dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
while True:
    ans[current_pos[0]][current_pos[1]] = current_num
    dx, dy = dxy[status % 4]
    next_pos = [current_pos[0] + dx, current_pos[1] + dy]
    if 0 <= next_pos[0] < n and 0 <= next_pos[1] < n:
        if ans[next_pos[0]][next_pos[1]] == "T":
            break
        elif ans[next_pos[0]][next_pos[1]] == 0:
            ans[next_pos[0]][next_pos[1]] = current_num
            current_pos = next_pos
            current_num += 1
        else:
            status += 1
    else:
        status += 1
out = []
for ansi in ans:
    out.append(" ".join(map(str, ansi)))
print(*out, sep="\n")
