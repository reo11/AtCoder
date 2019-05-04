h, w = map(int, input().split())

a = [list(str(input())) for i in range(h)]
pre_a = [x[:] for x in a]
ans = 0

while True:
    count_dot = 0
    for i in range(h):
        for j in range(w):
            if pre_a[i][j] == "#":
                if i - 1 >= 0:
                    a[i-1][j] = "#"
                if i + 1 <= h-1:
                    a[i+1][j] = "#"
                if j - 1 >= 0:
                    a[i][j-1] = "#"
                if j + 1 <= w-1:
                    a[i][j+1] = "#"
            else:
                count_dot += 1
    pre_a = [x[:] for x in a]
    if count_dot > 0:
        ans += 1
    else:
        break
print(ans)
