from itertools import permutations

a = list(map(int, input().split()))

place = []
for i, v in enumerate(a):
    for j in range(v):
        place.append([i, j])

# 　全探索
def check(box):
    f = True
    for i in range(3):
        for j in range(2):
            if box[i][j] > box[i][j + 1]:
                f = False
    for j in range(3):
        for i in range(2):
            if box[i][j] > box[i + 1][j]:
                f = False
    return f


count = 0
for v in permutations(place):
    box = [[100 for _ in range(3)] for _ in range(3)]
    for i, (x, y) in enumerate(v):
        box[x][y] = i + 1
    if check(box):
        count += 1
print(count)
