from copy import deepcopy
n = int(input())
s = input().rstrip()

def solve1(n, s):
    # 全探索
    cnt = 0
    for v in range(0, 1000):
        v = str(v)
        v = "0" * (3 - len(v)) + v
        idx = 0
        for i in range(len(s)):
            if s[i] == v[idx]:
                idx += 1
            if idx == 3:
                cnt += 1
                break
    print(cnt)

def solve2(n, s):
    # DP
    dp = [[[False for _ in range(1000)] for _ in range(4)] for _ in range(n+1)]
    dp[0][0][0] = True

    for i in range(n):
        for j in range(3):
            for k in range(100):
                if dp[i][j][k]:
                    num = k*10 + int(s[i])
                    dp[i+1][j+1][num] = True
        for j in range(4):
            for k in range(1000):
                dp[i+1][j][k] |= dp[i][j][k]

    cnt = 0
    for i in range(1000):
        if dp[n][3][i]:
            cnt += 1
    print(cnt)

solve2(n, s)