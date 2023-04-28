import sys
from collections import defaultdict
from pprint import pprint
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)
MOD = 998244353

s = list(input())
n = len(s)
memo = defaultdict(lambda: -1)
alphabets = [chr(ord('a') + i) for i in range(26)]

for i in reversed(range(n + 1)):
    for c in alphabets:
        if s[i - 1] == c:
            memo[f"{i}_{c}"] = i
        else:
            memo[f"{i}_{c}"] = memo[f"{i + 1}_{c}"]

def sigma(idx, c):
    # idxより右で初めてcが出現するi
    pattern = f"{idx}_{c}"
    return memo[pattern]

# 配るDP
ans = 0
for x in range(1, n):
    # S1はxより左だけで構成される
    # S2はxを含む右で構成される
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # ''と''を部分列の初期状態として定義
    dp[0][x] = 1
    for i in range(n):
        for j in range(i + 1, n):
            for c in alphabets:
                i_sigma = sigma(i + 1, c)
                if i_sigma > x:
                    # xより左だけで構成しないといけない
                    continue
                j_sigma = sigma(j + 1, c)
                # print(c, " ", i_sigma, " ", j_sigma)
                if i_sigma == -1 or j_sigma == -1:
                    # i, jより右にcが存在しない
                    continue
                dp[i_sigma][j_sigma] += dp[i][j]
                dp[i_sigma][j_sigma] %= MOD
    for i in range(x, n + 1):
        ans += dp[x][i]
        ans %= MOD

pprint(ans)