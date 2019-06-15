n = int(input())
ga, sa, ba = map(int, input().split())
gb, sb, bb = map(int, input().split())

dp1 = [0] * (n + 1)
if n > 5001:
    for i in range(1, 5001):
        feat = [i]
        if i - ga >= 0:
            feat.append(dp1[i-ga]+gb)
        if i - sa >= 0:
            feat.append(dp1[i-sa]+sb)
        if i - ba >= 0:
            feat.append(dp1[i-ba]+bb)
        dp[i] = max(feat)
    for i in range(5001, n+1):
        dp1[i] = max(i, dp1[i-ga]+gb, dp1[i-sa]+sb, dp1[i-ba]+bb)
else:
    for i in range(1, n+1):
        feat = [i]
        if i - ga >= 0:
            feat.append(dp1[i-ga]+gb)
        if i - sa >= 0:
            feat.append(dp1[i-sa]+sb)
        if i - ba >= 0:
            feat.append(dp1[i-ba]+bb)
        dp1[i] = max(feat)

B = dp1[-1]
dp2 = [0] * (B + 1)
if B > 5001:
    for i in range(1, 5001):
        feat = [i]
        if i - gb >= 0:
            feat.append(dp2[i-gb]+ga)
        if i - sb >= 0:
            feat.append(dp2[i-sb]+sa)
        if i - bb >= 0:
            feat.append(dp2[i-bb]+ba)
        dp2[i] = max(feat)

    for i in range(5001, B+1):
        dp2[i] = max(i, dp2[i-gb]+ga, dp2[i-sb]+sa, dp2[i-bb]+ba)
else:
    for i in range(1, B+1):
        feat = [i]
        if i - gb >= 0:
            feat.append(dp2[i-gb]+ga)
        if i - sb >= 0:
            feat.append(dp2[i-sb]+sa)
        if i - bb >= 0:
            feat.append(dp2[i-bb]+ba)
        dp2[i] = max(feat)

print(dp2[-1])
