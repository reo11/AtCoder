h, w = map(int, input().split())

a = [list(str(input())) for i in range(h)]
pre_a = [x[:] for x in a]

edit_list = []
for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            edit_list.append([i, j])
pre_edit_list = [x[:] for x in edit_list]

ans = 0

while True:
    edit_list = []
    count_dot = 0
    for (i, j) in pre_edit_list:
        if i - 1 >= 0:
            a[i-1][j] = "#"
            if pre_a[i-1][j] != "#":
                edit_list.append([i-1, j])
                count_dot += 1
        if i + 1 <= h-1:
            a[i+1][j] = "#"
            if pre_a[i+1][j] != "#":
                edit_list.append([i+1, j])
                count_dot += 1
        if j - 1 >= 0:
            a[i][j-1] = "#"
            if pre_a[i][j-1] != "#":
                edit_list.append([i, j-1])
                count_dot += 1
        if j + 1 <= w-1:
            a[i][j+1] = "#"
            if pre_a[i][j+1] != "#":
                edit_list.append([i, j+1])
                count_dot += 1
    pre_a = [x[:] for x in a]
    pre_edit_list = [x[:] for x in edit_list]

    if count_dot > 0:
        ans += 1
    else:
        break
print(ans)

