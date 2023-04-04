n, m = map(int, input().split())

dp = [[-1 for _ in range(n + 1)] for _ in range(10)]

# num, n
ans = [-1, -1]

for num in range(1, 10):
    amari = num % m
    for i in range(1, n + 1):
        if i > 1:
            amari = (amari * 10) % m
        if dp[num][i - 1] == -1:
            dp[num][i] = amari % m
        else:
            dp[num][i] = (dp[num][i - 1] + amari) % m

        if dp[num][i] == 0:
            if i > ans[1]:
                ans = [num, i]
            elif i == ans[1] and num > ans[0]:
                ans = [num, i]

if ans[0] == -1:
    print(-1)
else:
    s = ""
    for i in range(ans[1]):
        s += str(ans[0])
    print(s)
