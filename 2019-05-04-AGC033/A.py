h, w = map(int, input().split())

a = [list(str(input())) for i in range(h)]
edit_list = []

for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            edit_list.append([i, j])
pre_edit_list = [x[:] for x in edit_list]
ans = 0
while edit_list != []:
    ans += 1
    edit_list = []
    for (i, j) in pre_edit_list:
        if i-1 >= 0 and a[i-1][j] != "#":
            a[i-1][j] = "#"
            edit_list.append([i-1, j])
        if i+1 <= h-1 and a[i+1][j] != "#":
            a[i+1][j] = "#"
            edit_list.append([i+1, j])
        if j-1 >= 0 and a[i][j-1] != "#":
            a[i][j-1] = "#"
            edit_list.append([i, j-1])
        if j+1 <= w-1 and a[i][j+1] != "#":
            a[i][j+1] = "#"
            edit_list.append([i, j+1])
        pre_edit_list = [x[:] for x in edit_list]

print(ans-1)
