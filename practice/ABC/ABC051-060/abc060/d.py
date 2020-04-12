import sys
from collections import defaultdict
input = sys.stdin.buffer.readline

n, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]

pre_dp = defaultdict(lambda: 0)
pre_dp[0] = 0

for i in range(1, n+1):
    cur_dp = defaultdict(lambda: 0)
    w_i, v_i = wv[i-1]

    keys = sorted(pre_dp.keys())
    for k in keys:
        cur_dp[k] = max(cur_dp[k], pre_dp[k])
        if k + w_i <= W:
            big = max(pre_dp[k + w_i], pre_dp[k] + v_i)
            cur_dp[k+w_i] = big
    pre_dp = cur_dp
ans = 0
for w, v in cur_dp.items():
    if w <= W:
        ans = max(ans, v)

print(ans)

