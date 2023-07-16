import sys
from math import ceil, floor

input = sys.stdin.readline

h, n = map(int, input().split())
abc = []
max_a = 0
for i in range(n):
    a, b = map(int, input().split())
    c = a / b
    abc.append([a, b, c])
    max_a = max(a, max_a)

best = sorted(abc, key=lambda x: x[2], reverse=True)[0]
cost = 0
abc.sort()

while h > 0:
    if h > best[0]:
        h -= best[0]
        cost += best[1]
    else:
        c = 1000000
        for i in range(n):
            if h - abc[i][0] > 0:
                best_a = floor((h - abc[i][0]) / best[0])
                c = min(
                    c,
                    best_a * best[1]
                    + abc[i][1] * ceil((h - best_a * best[0]) / abc[i][0]),
                )
            else:
                c = min(c, abc[i][1] * ceil(h / abc[i][0]))
        cost += c
        h = -1
print(cost)
