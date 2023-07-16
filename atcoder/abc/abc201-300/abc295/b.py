r, c = map(int, input().split())
b = []
for i in range(r):
    b.append(list(input()))


def print_board(b):
    for i in range(len(b)):
        print("".join(b[i]))


def distance(x1, y1, x2, y2):
    return abs(y2 - y1) + abs(x2 - x1)


not_targets = set(["#", "."])
# solve
for j in range(r):
    for i in range(c):
        # 爆弾全探索
        if b[j][i] in not_targets:
            continue
        bomb = int(b[j][i])
        min_i = max(0, i - bomb)
        max_i = min(c - 1, i + bomb)
        min_j = max(0, j - bomb)
        max_j = min(r - 1, j + bomb)
        for sub_j in range(min_j, max_j + 1):
            for sub_i in range(min_i, max_i + 1):
                if distance(j, i, sub_j, sub_i) <= bomb and b[sub_j][sub_i] == "#":
                    b[sub_j][sub_i] = "."

for j in range(r):
    for i in range(c):
        if b[j][i] not in not_targets:
            b[j][i] = "."

print_board(b)
