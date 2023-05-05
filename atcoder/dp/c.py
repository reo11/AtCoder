n = int(input())
dp = [[0 for _ in range(3)] for _ in range(n + 1)]

for date in range(1, n + 1):
    abc = map(int, input().split()) # 入力を取得しながら更新
    for today_action in range(3):
        for yesterday_action in range(3):
            if today_action == yesterday_action:
                continue # 同じ活動はできない
            dp[date][today_action] = max(dp[date][today_action], dp[date - 1][yesterday_action] + abc[today_action])
print(max(dp[-1]))