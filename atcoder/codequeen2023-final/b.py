from collections import defaultdict

n = int(input())
rc = []


def four(x, y):
    # x, yを入れたら縦横斜めの座標系に変換する
    r1 = x + y
    r2 = (n - 1 - x) + y
    return [x, y, r1, r2]


ans = [-1, -1]
flag = True
memo = defaultdict(lambda: defaultdict(lambda: False))
for _ in range(n - 1):
    r, c = map(int, input().split())
    rc.append([r - 1, c - 1])
    v = four(r - 1, c - 1)
    for i, v_i in enumerate(v):
        if memo[i][v_i]:
            flag = False
        memo[i][v_i] = True

flag = False
for x in range(n):
    for y in range(n):
        r1 = x + y
        r2 = (n - 1 - x) + y
        if not memo[0][x] and not memo[1][y] and not memo[2][r1] and not memo[3][r2]:
            ans = [x + 1, y + 1]
            flag = True
            break
    if flag:
        break
if ans == [-1, -1]:
    print(-1)
else:
    print(f"{ans[0]} {ans[1]}")
