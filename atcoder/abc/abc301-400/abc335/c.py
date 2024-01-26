import sys

import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
input = lambda: sys.stdin.readline().rstrip()

directions = {"L": [-1, 0], "R": [1, 0], "U": [0, 1], "D": [0, -1]}

n, q = map(int, input().split())
queries = []
for _ in range(q):
    query_type, x = input().split()
    queries.append((query_type, x))

ans = []
dragon = []
for i in reversed(range(1, n + 1)):
    dragon.append([i, 0])

for query_type, x in queries:
    if query_type == "1":
        next_head_x = dragon[-1][0] + directions[x][0]
        next_head_y = dragon[-1][1] + directions[x][1]
        dragon.append([next_head_x, next_head_y])
    else:
        x = int(x)
        current_x = dragon[-x]
        ans.append(f"{current_x[0]} {current_x[1]}")
print(*ans, sep="\n")
