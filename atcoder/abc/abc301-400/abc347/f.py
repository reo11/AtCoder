# imos法で全てを数え上げる
# 上位から３択を適当にやるといけそう
n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

# 2次元imos法
imos = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        imos[i + 1][j + 1] = A[i][j] + imos[i + 1][j] + imos[i][j + 1] - imos[i][j]

# MxMの範囲の総和を、(n - m) * (n - m)通り全て求める
sums = [[0 for _ in range(n - m + 1)] for _ in range((n - m + 1))]
for i in range(n - m + 1):
    for j in range(n - m + 1):
        x1, y1 = j, i
        x2, y2 = j + m, i + m
        sums[i][j] = imos[y2][x2] - imos[y2][x1] - imos[y1][x2] + imos[y1][x1]

def is_in_same_area(yi, xi, yj, xj):

    return (yi - min(yi, yj)) // m == (yj - min(yi, yj)) // m and \
        (xi  - min(xi, xj)) // m == (xj  - min(xi, xj)) // m

ans = 0
for yi in range(len(sums)):
    for xi in range(len(sums)):
        for yj in range(yi, len(sums)):
            for xj in range(len(sums)):
                if is_in_same_area(yi, xi, yj, xj):
                    continue
                for yk in range(yj, len(sums)):
                    for xk in range(len(sums)):
                        if is_in_same_area(yi, xi, yk, xk) or is_in_same_area(yj, xj, yk, xk):
                            continue
                        ans = max(ans, sums[yi][xi] + sums[yj][xj] + sums[yk][xk])

print(ans)
