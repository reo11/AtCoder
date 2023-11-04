a = [list(map(int, input().split())) for _ in range(9)]


flag = True
# 行判定
for i in range(9):
    row_counts = set()
    for j in range(9):
        row_counts.add(a[i][j])
    if len(row_counts) != 9:
        flag = False
# 列判定
for i in range(9):
    row_counts = set()
    for j in range(9):
        row_counts.add(a[j][i])
    if len(row_counts) != 9:
        flag = False

# 3x3判定
for i in range(3):
    for j in range(3):
        row_counts = set()
        for k in range(3):
            for l in range(3):
                row_counts.add(a[i * 3 + k][j * 3 + l])
        if len(row_counts) != 9:
            flag = False

if flag:
    print("Yes")
else:
    print("No")