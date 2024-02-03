from collections import defaultdict, deque
INF = float("inf")
n = int(input())
s = [list(input()) for _ in range(n)]
players = []

for i in range(n):
    for j in range(n):
        if s[i][j] == "P":
            players.append((i, j))

# 4方向の移動
dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
min_costs = [[[[INF for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
q = deque([players])

def move(pos, dx, dy):
    next_x = pos[0] + dx
    next_y = pos[1] + dy
    if next_x < 0 or next_x >= n:
        return pos
    elif next_y < 0 or next_y >= n:
        return pos
    elif s[next_x][next_y] == "#":
        return pos
    else:
        return (next_x, next_y)

min_costs[players[0][0]][players[0][1]][players[1][0]][players[1][1]] = 0

while q:
    players = q.popleft()
    cost = min_costs[players[0][0]][players[0][1]][players[1][0]][players[1][1]]

    for dx, dy in dxy:
        next_player1 = move(players[0], dx, dy)
        next_player2 = move(players[1], dx, dy)
        if min_costs[next_player1[0]][next_player1[1]][next_player2[0]][next_player2[1]] != INF:
            # 訪問済み
            continue
        if next_player1 == players[0] and next_player2 == players[1]:
            continue
        if next_player1 == next_player2:
            print(cost + 1)
            exit()
        min_costs[next_player1[0]][next_player1[1]][next_player2[0]][next_player2[1]] = cost + 1
        q.append([next_player1, next_player2])
print(-1)
