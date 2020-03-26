w = int(input())
n, k = map(int, input().split())
ab = [input().split() for _ in range(n)]
ab = [(int(x[0]), int(x[1])) for x in ab]
ab = list(filter(lambda x: x[0] <= w, ab))

dp = [[[0 for _ in range(w+1)] for _ in range(k+1)] for _ in range(2)]

for j in range(len(ab)):
    for l in range(k):
        for i in range(w+1):
            w_i = ab[j][0]
            v_i = ab[j][1]
            if i + w_i <= w:
                dp[1][l+1][i+w_i] = max(dp[0][l+1][i+w_i], dp[0][l][i]+v_i)
    for l in range(k+1):
        for i in range(w+1):
            dp[0][l][i] = dp[1][l][i]

print(max(dp[1][k]))