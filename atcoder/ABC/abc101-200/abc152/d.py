n = int(input())

c = [[0 for _ in range(10)] for _ in range(10)]
for k in range(1, n+1):
    s = str(k)
    c[int(s[0])][int(s[-1])] += 1
ans = 0
for i in range(10):
    for j in range(10):
        ans += c[i][j] * c[j][i]
print(ans)
