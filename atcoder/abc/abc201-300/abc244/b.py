n = int(input())
t = input()

ans = [0, 0]
dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
status = 1
for i in range(n):
    ti = t[i]
    if ti == "S":
        y, x = dxy[status % 4]
        ans[0] += x
        ans[1] += y
    else:
        status += 1
print(*ans, sep=" ")
