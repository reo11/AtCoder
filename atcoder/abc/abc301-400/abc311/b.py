n, d = map(int, input().split())
s = [list(input()) for _ in range(n)]
x = [0 for _ in range(d)]
for i in range(n):
    for j in range(d):
        if s[i][j] == 'x':
            x[j] += 1

ans = 0
count = 0
for x_i in x:
    if x_i == 0:
        count += 1
        ans = max(ans, count)
    else:
        count = 0
print(ans)
    