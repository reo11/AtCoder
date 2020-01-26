import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    xy = []
    for j in range(n):
        x, y = map(int, input().split())
        xy.append((min(x, y), x, y))
    xy.sort()

    cur_xy = (0, 0)
    ans = ""
    flag = True
    for key, x, y in xy:
        cur_x, cur_y = cur_xy
        if cur_x <= x:
            ans += "R" * (x - cur_x)
            cur_x = x
        else:
            flag = False
        if cur_y <= y:
            ans += "U" * (y - cur_y)
            cur_y = y
        else:
            flag = False
        if not flag:
            break
        cur_xy = (cur_x, cur_y)
    if flag:
        print("YES")
        print(ans)
    else:
        print("NO")

