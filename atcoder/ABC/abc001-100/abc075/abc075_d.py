n, k = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(n)]

MAX = 10 ** 9
MIN = -1 * MAX


def check(x_r, x_l, y_t, y_b):
    tl = [MIN, MAX]
    br = [MAX, MIN]
    if x_r == x_l or y_t == y_b:
        return False, -1

    tl[0] = max(tl[0], xy[x_l][0])
    tl[1] = min(tl[1], xy[y_t][1])
    br[0] = min(br[0], xy[x_r][0])
    br[1] = max(br[1], xy[y_b][1])

    # count k
    cnt = 0
    for i in range(n):
        if tl[0] <= xy[i][0] <= br[0] and br[1] <= xy[i][1] <= tl[1]:
            cnt += 1
    if cnt < k:
        return False, -1
    area = (br[0] - tl[0]) * (tl[1] - br[1])
    return True, area


INF = 10 ** 20
ans = INF
for a in range(n):
    for b in range(n):
        if a == b:
            continue
        if xy[a][0] < xy[b][0]:
            continue
        for c in range(n):
            for d in range(n):
                if c == d:
                    continue
                if xy[c][1] < xy[d][1]:
                    continue
                f, area = check(a, b, c, d)
                if f:
                    ans = min(ans, area)
print(ans)
