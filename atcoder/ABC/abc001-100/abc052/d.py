n, a, b = map(int, input().split())
x = list(map(int, input().split()))

cost = 0
cur_x = x[0]
for i in range(1, n):
    cost += min((x[i] - cur_x) * a, b)
    cur_x = x[i]
print(cost)