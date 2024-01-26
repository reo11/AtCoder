from collections import defaultdict

MOD = 998244353
s = list(input())

# sは?, (, )で構成され、?は(か)に置き換えることができる
# sを括弧列にする方法は何通りあるか

# dp
# 最後の方は考えなくていい括弧があるので、defaultdictで管理する
# それまでに開いた状態の括弧の数で管理して、最後に0のものを数える
dp = defaultdict(lambda: defaultdict(lambda: 0))
dp[0][0] = 1

for i in range(1, len(s) + 1):
    # i文字目
    s_i = s[i - 1]
    for j in dp[i - 1].keys():
        # もし残りの文字列が開いている括弧の数よりも少ない場合は、生成不可能なのでスキップする
        # 場合の数が正のものから配るDPをする
        if s_i == "(":
            dp[i][j + 1] += dp[i - 1][j]
            dp[i][j + 1] %= MOD
        elif s_i == ")":
            if j > 0:
                dp[i][j - 1] += dp[i - 1][j]
                dp[i][j - 1] %= MOD
            else:
                continue
        else:
            if j - 1 < len(s) - i:
                dp[i][j + 1] += dp[i - 1][j]
                dp[i][j + 1] %= MOD
            if j > 0:
                dp[i][j - 1] += dp[i - 1][j]
                dp[i][j - 1] %= MOD
print(dp[len(s)][0])
