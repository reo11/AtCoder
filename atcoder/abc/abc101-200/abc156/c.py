n = int(input())
x = list(map(int, input().split()))


ans = 10 ** 12
for i in range(1, 101):
    cost = 0
    for j in range(n):
        cost += (x[j] - i) ** 2
    ans = min(ans, cost)
print(ans)
