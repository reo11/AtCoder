x, y, w = input().split()
x = int(x) - 1
y = int(y) - 1
c = [[i for i in list(input())] for i in range(9)]

ans = []
ud = ""
lr = ""
if len(w) == 1:
    if w in ["L", "R"]:
        lr = w
    else:
        ud = w
else:
    lr = w[0]
    ud = w[1]

for i in range(4):
    ans.append(str(c[y][x]))
    if lr == "L" and x == 0:
        lr = "R"
        x = 1
    elif lr == "R" and x == 8:
        lr = "L"
        x = 7
    elif lr == "L":
        x -= 1
    elif lr == "R":
        x += 1

    if ud == "U" and y == 0:
        ud = "D"
        y = 1
    elif ud == "D" and y == 8:
        ud = "U"
        y = 7
    elif ud == "U":
        y -= 1
    elif ud == "D":
        y += 1
print("".join(ans))