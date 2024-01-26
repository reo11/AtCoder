import sys

import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n, c = map(int, input().split())
ta = []
for _ in range(n):
    t, a = map(int, input().split())
    ta.append((t, a))

bit_transformations = [[[i for i in range(2)] for _ in range(30)] for _ in range(n + 1)]

for i in range(1, n + 1):
    op_type, ai = ta[i - 1]
    for j in range(30):
        ai_bit = (ai >> j) & 1
        for k in range(2):
            if op_type == 1:
                bit_transformations[i][j][k] = bit_transformations[i - 1][j][k] & ai_bit
            elif op_type == 2:
                bit_transformations[i][j][k] = bit_transformations[i - 1][j][k] | ai_bit
            else:
                bit_transformations[i][j][k] = bit_transformations[i - 1][j][k] ^ ai_bit


ans = []
x = c
for i in range(1, n + 1):
    next_x = 0
    for j in range(30):
        target_bit = (x >> j) & 1
        transformed_bit = bit_transformations[i][j][target_bit]
        next_x += transformed_bit << j
    x = next_x
    ans.append(x)
print(*ans, sep="\n")
