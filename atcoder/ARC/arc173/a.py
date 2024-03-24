# 二分探索

def under_neq_number_count(x):
    # x以下のneq_numberの個数を返す
    # 桁DP
    # dp[i-th number][is_max][i-th number is j]
    num = str(x)
    dp = [[[0 for _ in range(10)] for _ in range(2)] for _ in range(len(num) + 1)]
    dp[0][0][0] = 1
    dp[0][1][0] = 1
    for i in range(len(num)):
        D = int(num[i])
        for j in range(2):
            for k in range(10):
                for d in range(10 if j else D + 1):
                    if d != k:
                        dp[i + 1][j or (d < D)][d] += dp[i][j][k]
    print(dp)
print(under_neq_number_count(25))