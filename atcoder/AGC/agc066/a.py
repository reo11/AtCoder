from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
INF = float("inf")
n, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
max_cost = d * n * n // 2

dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def check(a, cost):
    # すべてのマスの差がd以上
    is_valid = True
    for i in range(n):
        for j in range(n):
            for di, dj in dxy:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= n or nj < 0 or nj >= n:
                    continue
                if abs(a[i][j] - a[ni][nj]) < d:
                    return False
    return n * n * d // 2 >= cost

def solve(n, d, a):
    # 初期地点を決める
    q = []
    heapify(q)
    versions = defaultdict(lambda: defaultdict(lambda: 0))

    for i in range(n):
        for j in range(n):
            cost_ij = 0
            is_valid = True
            max_num = -INF
            min_num = INF
            for di, dj in dxy:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= n or nj < 0 or nj >= n:
                    continue
                max_num = max(max_num, a[ni][nj])
                min_num = min(min_num, a[ni][nj])
                if abs(a[i][j] - a[ni][nj]) < d:
                    is_valid = False
            if not is_valid:
                next_high = max_num + d
                next_low = min_num - d
                cost_ij = min(abs(next_high - a[i][j]), abs(next_low - a[i][j]))
            else:
                cost_ij = 0
            version = 1
            heappush(q, [cost_ij, i, j, version])
            versions[i][j] = version

    visited = [[False] * n for _ in range(n)]
    cost = 0
    while q:
        i, j, version = heappop(q)[1:]
        if visited[i][j]:
            continue
        if versions[i][j] != version:
            continue

        visited[i][j] = True

        # 周りより大きく/小さくする
        is_valid = True
        max_num = -INF
        min_num = INF
        for di, dj in dxy:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= n:
                continue
            if abs(a[i][j] - a[ni][nj]) < d:
                is_valid = False
            max_num = max(max_num, a[ni][nj])
            min_num = min(min_num, a[ni][nj])
            # if not visited[ni][nj]:
            #     q.append([ni, nj])

        if not is_valid:
            next_high = max_num + d
            next_low = min_num - d

            if abs(next_high - a[i][j]) < abs(next_low - a[i][j]):
                cost += abs(next_high - a[i][j])
                a[i][j] = next_high
            else:
                cost += abs(next_low - a[i][j])
                a[i][j] = next_low

            # 周辺のコストを更新
            for di, dj in dxy:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= n or nj < 0 or nj >= n:
                    continue
                max_num = -INF
                min_num = INF
                is_valid = True
                for dii, djj in dxy:
                    nii, njj = ni + dii, nj + djj
                    if nii < 0 or nii >= n or njj < 0 or njj >= n:
                        continue
                    if abs(a[ni][nj] - a[nii][njj]) < d:
                        is_valid = False
                    max_num = max(max_num, a[nii][njj])
                    min_num = min(min_num, a[nii][njj])
                if not is_valid:
                    next_high = max_num + d
                    next_low = min_num - d
                    cost_ij = min(abs(next_high - a[ni][nj]), abs(next_low - a[ni][nj]))
                else:
                    cost_ij = 0
                versions[ni][nj] += 1
                heappush(q, [cost_ij, nii, njj, versions[ni][nj]])

        # print(i, j, cost)
        # print(*a, sep="\n")
    return [cost, a]

cost, ans_a = solve(n, d, a)
ans = []
for row in ans_a:
    ans.append(" ".join(map(str, row)))
print(*ans, sep="\n")
# print(cost, ans_a)
# print(check(ans_a, cost))