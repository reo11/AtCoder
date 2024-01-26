n, k = map(int, input().split())
p = list(map(int, input().split()))
for i in range(n):
    p[i] = p[i] - 1
c = list(map(int, input().split()))

# 2の30乗まで調べれば十分
until = 0
for i in range(31):
    if 2**i <= k:
        until = i
memo = [[[0, 0] for _ in range(n)] for _ in range(until + 1)]
ans = [[i, 0] for i in range(n)]

for i in range(until):
    if i == 0:
        for idx in range(n):
            memo[i][idx][0] = p[idx]
            memo[i][idx][1] = c[idx]
    for idx in range(n):
        p_i = memo[i][idx][0]
        memo[i + 1][p_i][0] = memo[i][idx][0]
        memo[i + 1][p_i][1] = memo[i][idx][1] + memo[i][p_i][1]

for i in reversed(range(until)):
    if 2**i <= k:
        next_ans = [[i, 0] for i in range(n)]
        for idx in range(len(ans)):
            p_i = ans[idx][0]
            score = ans[idx][1]
            next_pi = memo[i][p_i][0]
            next_score = score + memo[i][p_i][1]
            next_ans[idx][0] = next_pi
            next_ans[idx][1] = next_score
        ans = next_ans
        k -= 2**i
print(memo)
print(ans)
