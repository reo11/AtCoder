n = int(input())
MOD = 998244353
cards = []
for _ in range(n):
    a, b = map(int, input().split())
    cards.append([a, b])

# DPっぽい
# i枚目まで見た時の組み合わせを適当に更新

dp = [[0, 0] for _ in range(n + 1)]
dp[0] = [1, 1]
dp[1] = [1, 1]

for i in range(2, n + 1):
    next_a = 0
    next_b = 0

    # i - 2枚目のカードの表面（A_{i-2}）
    if cards[i - 2][0] != cards[i - 1][0]:
        next_a += dp[i - 1][0]
    if cards[i - 2][0] != cards[i - 1][1]:
        next_b += dp[i - 1][0]
    # i - 2枚目のカードの裏面（B_{i-2}）
    if cards[i - 2][1] != cards[i - 1][0]:
        next_a += dp[i - 1][1]
    if cards[i - 2][1] != cards[i - 1][1]:
        next_b += dp[i - 1][1]
    dp[i] = [next_a % MOD, next_b % MOD]
print((dp[-1][0] + dp[-1][1]) % MOD)
