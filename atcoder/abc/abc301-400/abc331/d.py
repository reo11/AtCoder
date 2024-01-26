import sys

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n, q = map(int, input().split())
p = [list(input()) for i in range(n)]
queries = []

for _ in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

# B -> 1, W -> 0
p = [[1 if p[i][j] == "B" else 0 for j in range(n)] for i in range(n)]
# 2N * 2Nに拡張
tmp_p = [[0 for _ in range(2 * n)] for _ in range(2 * n)]
for i in range(n):
    for j in range(n):
        tmp_p[i][j] = p[i][j]
        tmp_p[i + n][j] = p[i][j]
        tmp_p[i][j + n] = p[i][j]
        tmp_p[i + n][j + n] = p[i][j]
p = tmp_p
# 2次元imos法
imos = [[0 for _ in range(2 * n + 1)] for _ in range(2 * n + 1)]
for i in range(2 * n):
    for j in range(2 * n):
        imos[i + 1][j + 1] = p[i][j] + imos[i + 1][j] + imos[i][j + 1] - imos[i][j]


def solve_query(query):
    x1, y1, x2, y2 = query
    # 基準点を(0, 0)にする
    mod_x1 = x1 % n
    mod_y1 = y1 % n
    x2 = x2 - x1 + mod_x1
    y2 = y2 - y1 + mod_y1
    x1 = mod_x1
    y1 = mod_y1
    # 4つの領域に分ける
    y_max = y2 + (n - (y2 % n))
    x_max = x2 + (n - (x2 % n))
    ret = 0

    # 4隅
    ret += imos[(y2 % n)][(x2 % n)]
    ret += imos[(y2 % n)][n - (x1 % n)]
    ret += imos[(y2 % n)][x1]
    ret += imos[y1][x_max]

    ret += imos[n][n] * (((y2 - y1) // n)) * ((x2 - x1) // n)

    return ret


ans = []
for query in queries:
    ans.append(solve_query(query))
print(*ans, sep="\n")
