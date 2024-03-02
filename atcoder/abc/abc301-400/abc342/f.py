n, l, d = map(int, input().split())

# ブラックジャックの勝率をDPする
# dp[i][j]: プレイヤーのスコアがi、ディーラーのスコアがjの時の勝率
# 逆からDPする

dealer_dp = [0] * (n + d + 1)
player_dp = [0] * (n + 1)
dealer_dp[0] = 1.0

# dp[i]: ディーラーのスコアがiになる確率
for i in range(l):
    for j in range(i + 1, i + 1 + d):
        dealer_dp[j] += dealer_dp[i] / d
    dealer_dp[i] = 0.0

for i in range(n):
    dealer_win_prob = 0.0
    for j in range(i + 1, n):
        dealer_win_prob += dealer_dp[j]
    player_dp[i] = 1.0 - dealer_win_prob

print(dealer_dp)
print(player_dp)