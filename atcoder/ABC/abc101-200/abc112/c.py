N = int(input())

x = [0] * N
y = [0] * N
h = [0] * N

for i in range(N):
    xyh = list(map(int, input().split()))
    x[i] = xyh[0]
    y[i] = xyh[1]
    h[i] = xyh[2]
    if xyh[2] != 0:
        Cx = xyh[0]
        Cy = xyh[1]
        CH = xyh[2]

for i in range(101):
    for j in range(101):
        flag = True
        H = CH + abs(i - Cx) + abs(j - Cy)
        for k in range(N):
            if h[k] != max(H - abs(i - x[k]) - abs(j - y[k]), 0):
                flag = False
                break
        if flag:
            print(i, j, H)
