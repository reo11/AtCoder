import math
from collections import defaultdict
INF = float('inf')

n = int(input())
candidates = []
z_sum = 0
takahashi = 0

for _ in range(n):
    # x: 高橋派, y: 青木派, z: 議席数
    x, y, z = map(int, input().split())
    z_sum += z
    if x > y:
        takahashi += z
    else:
        candidates.append([math.ceil((x + y) / 2) - x, z])

# dp: i番目までで、j議席獲得するのに必要な最小の人数
dp = defaultdict(lambda: INF)
dp[takahashi] = 0
for cost, z in candidates:
    # i番目の選挙区で寝返らせる人数と得られる議席数
    dp_keys = sorted(list(dp.keys()), reverse=True)  # 2重選択を防ぐため後ろから
    for pre_z in dp_keys:
        dp[pre_z + z] = min(dp[pre_z + z], dp[pre_z] + cost)

ans = INF
for i in range(math.ceil(z_sum / 2), z_sum + 1):
    # 議席数が過半数以上の中から最小の人数を選ぶ
    ans = min(ans, dp[i])
print(ans)
