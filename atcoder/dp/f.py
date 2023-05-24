# from pprint import pprint
s = list(input())
t = list(input())

dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

for s_i in range(len(s) + 1):
    for t_i in range(len(t) + 1):
        if s_i == 0 or t_i == 0:
            continue
        if s[s_i - 1] == t[t_i - 1]:
            dp[s_i][t_i] = dp[s_i - 1][t_i - 1] + 1
        else:
            dp[s_i][t_i] = max(dp[s_i - 1][t_i], dp[s_i][t_i - 1])
ans = ""
s_i = len(s)
t_i = len(t)
while s_i > 0 and t_i > 0:
    if dp[s_i][t_i] == dp[s_i - 1][t_i]:
        s_i -= 1
    elif dp[s_i][t_i] == dp[s_i][t_i - 1]:
        t_i -= 1
    else:
        ans = s[s_i - 1] + ans
        s_i -= 1
        t_i -= 1
# pprint(dp)
print(ans)
