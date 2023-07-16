MOD = 998244353
s = list(input())

small_alphabets = set([chr(ord("a") + i) for i in range(26)])
large_alphabets = set([chr(ord("A") + i) for i in range(26)])

dp = [[0 for _ in range(29)] for _ in range(len(s) + 1)]

for i in range(29):
    dp[0][i] = 1

for i in range(len(s)):
    if s[i] in small_alphabets:
        # abc...
        dp[i + 1][0] = dp[i][0]
    elif s[i] in large_alphabets:
        # ABC...
        for j in range(26):
            if ord("A") + j != ord(s[i]):
                dp[i + 1][j + 1] = dp[i][j + 1]
            else:
                dp[i + 1][j + 1] = dp[i][j + 1]
    else:
        pass
        # ?
# all small
# all large
# large - small
