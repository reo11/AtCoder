import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)
n, q = map(int, input().split())
queries = []

ans = []
for _ in range(q):
    q_i = list(map(int, input().split()))
    queries.append(q_i)

trains = [[-1, -1] for _ in range(n + 1)]
for q_i in queries:
    if q_i[0] == 1:
        # 連結
        x = q_i[1]
        y = q_i[2]
        trains[x][1] = y
        trains[y][0] = x
    elif q_i[0] == 2:
        # 分離
        x = q_i[1]
        y = q_i[2]
        trains[x][1] = -1
        trains[y][0] = -1
    else:
        # 列挙
        x = q_i[1]

        # 自分が先頭の場合
        out = []
        while trains[x][0] != -1:
            x = trains[x][0]
        # dowhile suru
        while True:
            out.append(x)
            x = trains[x][1]
            if x == -1:
                break
        out = [str(x) for x in out]
        ans.append(f"{len(out)} {' '.join(out)}")

print(*ans, sep='\n')