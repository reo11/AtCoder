a, b = map(int, input().split())

def solve1(num):
    # a, b < 10,000
    count = 0
    for i in range(1, num+1):
        n_str = str(i)
        if n_str.count(str(4)) > 0 or n_str.count(str(9)) > 0:
            count += 1
    return count

def solve2(num):
    # a, b < 1,000,000,000,000,000,000,000,000,000
    # 左から桁DP
    # dp[i-th number][is_max][already include 4 or 9]
    n = len(str(num)) + 1
    dp = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(n)]
    dp[0][0][0] = 1
    for i in range(n-1):
        D = int(str(num)[i])
        for j in range(2):
            for k in range(2):
                for d in range(10 if j else D+1):
                    dp[i+1][j or (d < D)][k or d == 4 or d == 9] += dp[i][j][k]
    return dp[-1][0][1] + dp[-1][1][1]
print(solve2(b) - solve2(a-1))
