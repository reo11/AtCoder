n = int(input())
a = list(map(int, input().split()))
cur_a = a[0]
cost = 0
for i in range(1, n):
    if a[i] < cur_a:
        cost += (cur_a - a[i])
    cur_a = max(cur_a, a[i])
print(cost)
