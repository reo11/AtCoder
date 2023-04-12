from collections import defaultdict
s = input()
x, y = map(int, input().split())

# 分解する
process = [[], []]

num = 0
counter = 0
for c in list(s):
    if c == "F":
        counter += 1
    else:
        process[num].append(counter)
        counter = 0
        num = (num + 1) % 2
if counter > 0:
    process[num].append(counter)

dpx = defaultdict(lambda: defaultdict(lambda: False))
dpy = defaultdict(lambda: defaultdict(lambda: False))

# x方向でi番目の操作実行時に到達可能かをDP
dpx[0][0] = True
for i in range(1, len(process[0]) + 1):
    move_distance = process[0][i - 1]
    for num in dpx[i - 1].keys():
        if i > 1:
            dpx[i][num - move_distance] = True
        dpx[i][num + move_distance] = True

# y方向でi番目の操作実行時に到達可能かをDP
dpy[0][0] = True
for i in range(1, len(process[1]) + 1):
    move_distance = process[1][i - 1]
    for num in dpy[i - 1].keys():
        dpy[i][num - move_distance] = True
        dpy[i][num + move_distance] = True

if dpx[len(process[0])][x] and dpy[len(process[1])][y]:
    print("Yes")
else:
    print("No")