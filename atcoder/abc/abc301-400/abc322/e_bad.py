import copy
MAX_NUM = 6

n, k, p = map(int, input().split())
INF = 10 ** 18
cas = []
for _ in range(n):
    ca = list(map(int, input().split()))
    c = ca[0]
    a = ca[1:]
    cas.append((c, a))

# K重のDPをすれば良い?
# K=3の例　dp[i][j][k]: 1つ目のパラメータをi、2つ目のパラメータをj、3つ目のパラメータをkにするのにかかる最小のコスト
# 配るDPでやる
if k == 1:
    dp = [INF for _ in range(MAX_NUM)]
    dp[0] = 0
elif k == 2:
    dp = [[INF for _ in range(MAX_NUM)] for _ in range(MAX_NUM)]
    dp[0][0] = 0
elif k == 3:
    dp = [[[INF for _ in range(MAX_NUM)] for _ in range(MAX_NUM)] for _ in range(MAX_NUM)]
    dp[0][0][0] = 0
elif k == 4:
    dp = [[[[INF for _ in range(MAX_NUM)] for _ in range(MAX_NUM)] for _ in range(MAX_NUM)] for _ in range(MAX_NUM)]
    dp[0][0][0][0] = 0
else:
    dp = [[[[[INF for _ in range(MAX_NUM)] for _ in range(MAX_NUM)] for _ in range(MAX_NUM)] for _ in range(MAX_NUM)] for _ in range(MAX_NUM)]
    dp[0][0][0][0][0] = 0

for c, a in cas:
    tmp_dp = copy.deepcopy(dp)
    if k == 1:
        for i in range(6):
            idx1 = min(i + a[0], 5)
            tmp_dp[idx1] = min(tmp_dp[idx1], dp[i] + c)
    elif k == 2:
        for i in range(6):
            for j in range(6):
                idx1 = min(i + a[0], 5)
                idx2 = min(j + a[1], 5)
                tmp_dp[idx1][idx2] = min(tmp_dp[idx1][idx2], dp[i][j] + c)
    elif k == 3:
        for i in range(6):
            for j in range(6):
                for ii in range(6):
                    idx1 = min(i + a[0], 5)
                    idx2 = min(j + a[1], 5)
                    idx3 = min(ii + a[2], 5)
                    tmp_dp[idx1][idx2][idx3] = min(tmp_dp[idx1][idx2][idx3], dp[i][j][ii] + c)
    elif k == 4:
        for i in range(6):
            for j in range(6):
                for ii in range(6):
                    for jj in range(6):
                        idx1 = min(i + a[0], 5)
                        idx2 = min(j + a[1], 5)
                        idx3 = min(ii + a[2], 5)
                        idx4 = min(jj + a[3], 5)
                        tmp_dp[idx1][idx2][idx3][idx4] = min(tmp_dp[idx1][idx2][idx3][idx4], dp[i][j][ii][jj] + c)
    else:
        for i in range(6):
            for j in range(6):
                for ii in range(6):
                    for jj in range(6):
                        for kk in range(6):
                            idx1 = min(i + a[0], 5)
                            idx2 = min(j + a[1], 5)
                            idx3 = min(ii + a[2], 5)
                            idx4 = min(jj + a[3], 5)
                            idx5 = min(kk + a[4], 5)
                            tmp_dp[idx1][idx2][idx3][idx4][idx5] = min(tmp_dp[idx1][idx2][idx3][idx4][idx5], dp[i][j][ii][jj][kk] + c)
    dp = tmp_dp

ans = -1
if k == 1:
    for i in range(p, MAX_NUM):
        if dp[i] < INF:
            if ans == -1:
                ans = dp[i]
            else:
                ans = min(ans, dp[i])
elif k == 2:
    for i in range(p, MAX_NUM):
        for j in range(p, MAX_NUM):
            if dp[i][j] < INF:
                if ans == -1:
                    ans = dp[i][j]
                else:
                    ans = min(ans, dp[i][j])
elif k == 3:
    for i in range(p, MAX_NUM):
        for j in range(p, MAX_NUM):
            for ii in range(p, MAX_NUM):
                if dp[i][j][ii] < INF:
                    if ans == -1:
                        ans = dp[i][j][ii]
                    else:
                        ans = min(ans, dp[i][j][ii])
elif k == 4:
    for i in range(p, MAX_NUM):
        for j in range(p, MAX_NUM):
            for ii in range(p, MAX_NUM):
                for jj in range(p, MAX_NUM):
                    if dp[i][j][ii][jj] < INF:
                        if ans == -1:
                            ans = dp[i][j][ii][jj]
                        else:
                            ans = min(ans, dp[i][j][ii][jj])
else:
    for i in range(p, MAX_NUM):
        for j in range(p, MAX_NUM):
            for ii in range(p, MAX_NUM):
                for jj in range(p, MAX_NUM):
                    for kk in range(p, MAX_NUM):
                        if dp[i][j][ii][jj][kk] < INF:
                            if ans == -1:
                                ans = dp[i][j][ii][jj][kk]
                            else:
                                ans = min(ans, dp[i][j][ii][jj][kk])
print(ans)