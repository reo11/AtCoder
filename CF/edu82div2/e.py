from collections import defaultdict
T = int(input())
for i in range(T):
    s = str(input().rstrip())
    t = str(input().rstrip())
    s_d = defaultdict(int)
    t_d = defaultdict(int)

    for c in list(s):
        s_d[c] += 1
    for c in list(t):
        t_d[c] += 1
    f = False
    for c in list('abcdefghijklmnopqrstuvwxyz'):
        if s_d[c] < t_d[c]:
            f = True

    if f:
        print("NO")
        continue

    s3 = ""
    for i in range(2):
        s3 += s
    dp = [0 for _ in range(len(t) + 1)]
    for i in range(len(s3)):
        for j in range(len(t)):
            if s3[i] == t[j]:
                dp[j+1] = max(dp[j] + 1, dp[j+1])
    if dp[-1] == len(t):
        print("YES")
    else:
        print("NO")