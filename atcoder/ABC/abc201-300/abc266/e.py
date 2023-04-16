n = int(input())

# 期待値をDPする
# dp[N]: i回振った時の期待値の最大値
# 残りM回振って出る期待値と、今出ている目を比べる
# 前者の方が大きい場合は振り直す

dp = [0 for _ in range(101)]
for i in range(1, 101):
    for j in range(1, 7):
        dp[i] += max(j, dp[i - 1])
    dp[i] /= 6
print(dp[n])
