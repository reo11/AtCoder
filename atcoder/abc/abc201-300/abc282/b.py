n, m = map(int, input().split())
s = [list(input()) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        cnt = 0
        for k in range(m):
            if s[i][k] == "o" or s[j][k] == "o":
                cnt += 1
        if cnt == m:
            ans += 1
print(ans)
