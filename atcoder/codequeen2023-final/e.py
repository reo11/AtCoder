n = int(input())
a = list(map(int, input().split()))

# DPか貪欲
# 区間DPっぽいが、nが大きすぎる
# i番目まででj=0: i番目を使った場合の最大値, j=1: i番目を使わなかった場合の最大値
dp = [[0, 0] for _ in range(n + 1)]

for i in range(1, n + 1):
    # i番目が使用済みなので足すだけ
    dp[i][1] = dp[i - 1][0]
    # i番目を使っていない場合はiとi-1の