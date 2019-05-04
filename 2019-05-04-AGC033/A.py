import sys


def input():
    return sys.stdin.readline()[:-1]


h, w = map(int, input().split())

a = [list(str(input())) for i in range(h)]
black = []
for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            black.append([i, j])

ans = 0
min_ans = 0
for i in range(h):
    for j in range(w):
        min_dis = 10000000
        if a[i][j] == ".":
            for (x, y) in black:
                min_dis = min(abs(x - i) + abs(y - j), min_dis)
                if min_dis <= min_ans:
                    break
            ans = max(ans, min_dis)
            if min_dis > min_ans:
                min_ans = min_dis

print(ans)
