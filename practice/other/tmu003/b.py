# I - イウィ
from pprint import pprint
s = input()
n = len(s)

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for r in range(2, n+1):
    dp[0][r] = s[0:r]

pprint(dp)