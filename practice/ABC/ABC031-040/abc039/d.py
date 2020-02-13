import copy

h, w = map(int, input().split())
s = [[i for i in list(str(input()))] for i in range(h)]

pre_s = [['#' for _ in range(w)] for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            continue
        for dx in [-1, 0, 1]:
            x = j + dx
            if x < 0 or w-1 < x:
                continue
            for dy in [-1, 0, 1]:
                y = i + dy
                if y < 0 or h-1 < y:
                    continue
                pre_s[y][x] = '.'

tmp_s = copy.deepcopy(pre_s)
for i in range(h):
    for j in range(w):
        if pre_s[i][j] == '.':
            continue
        for dx in [-1, 0, 1]:
            x = j + dx
            if x < 0 or w-1 < x:
                continue
            for dy in [-1, 0, 1]:
                y = i + dy
                if y < 0 or h-1 < y:
                    continue
                tmp_s[y][x] = '#'

flag = True
for i in range(h):
    for j in range(w):
        if s[i][j] != tmp_s[i][j]:
            flag = False
            break
if flag:
    print("possible")
    for i in range(h):
        print("".join(pre_s[i]))
else:
    print("impossible")