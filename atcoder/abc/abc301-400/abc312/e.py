from collections import defaultdict

MAX_SIZE = 100
n = int(input())

l = []
for _ in [0] * n:
    l_i = list(map(lambda x: int(x) + 1, input().split()))
    l.append(l_i)


def iterations(x1, x2, y1, y2, z1, z2):
    for x in range(x1, x2):
        for y in range(y1, y2):
            for z in range(z1, z2):
                yield x, y, z


grid = [
    [[-1 for _ in range(MAX_SIZE + 2)] for _ in range(MAX_SIZE + 2)]
    for _ in range(MAX_SIZE + 2)
]
for i, (x1, y1, z1, x2, y2, z2) in enumerate(l, start=1):
    # 6面グリッドを埋めていく
    # x軸方向の面
    for x, y, z in iterations(x1, x2, y1, y2, z1, z2):
        grid[x][y][z] = i

ans = defaultdict(lambda: set())
for x, y, z in iterations(1, MAX_SIZE + 1, 1, MAX_SIZE + 1, 1, MAX_SIZE + 1):
    num1 = grid[x][y][z]
    # 6方向探索
    for dx, dy, dz in [
        [0, 0, 1],
        [0, 0, -1],
        [0, 1, 0],
        [0, -1, 0],
        [1, 0, 0],
        [-1, 0, 0],
    ]:
        num2 = grid[x + dx][y + dy][z + dz]
        if num1 == -1 or num2 == -1 or num1 == num2:
            continue
        ans[num1].add(num2)
        ans[num2].add(num1)

ans_out = []
for i in range(1, n + 1):
    ans_out.append(len(ans[i]))

print(*ans_out, sep="\n")
