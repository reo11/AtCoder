d = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

INF = 10**10
money = 0
ans = INF

for i in range(d):
    money += a[i]
    if money >= b[i]:
        ans = min(ans, b[i])

if ans == INF:
    print(-1)
else:
    print(ans)