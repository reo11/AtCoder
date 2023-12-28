import sys
import math
import itertools
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()
INF = float('inf')

n = int(input())
costs = defaultdict(lambda: defaultdict(lambda: 0))
for i in range(n - 1):
    di = list(map(int, input().split()))
    for j, j_num in enumerate(range(i + 1, n)):
        costs[i][j_num] = di[j]
        costs[j_num][i] = di[j]

# bitDP
dp = [-INF for _ in range(2 ** (n + 1))]
dp[0] = 0
ans = -INF
for bit in range(0, 2 ** (n + 1)):
    # 配るDP
    # 0のビットの位置を列挙
    zero_bits = []
    for i in range(n + 1):
        if bit & (1 << i) == 0:
            zero_bits.append(i)
    for bit_i, bit_j in itertools.combinations(zero_bits, 2):
        dp[bit | (1 << bit_i) | (1 << bit_j)] = max(dp[bit | (1 << bit_i) | (1 << bit_j)], dp[bit] + costs[bit_i][bit_j])
        ans = max(ans, dp[bit | (1 << bit_i) | (1 << bit_j)])
print(ans)