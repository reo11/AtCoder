n, x = map(int, input().split())
a = list(map(int, input().split()))

cost = 0
# if a[0] > x:
#     cost += a[0] - x
#     a[0] = x
for i in range(1, n):
    if a[i-1] + a[i] > x:
        c = a[i-1] + a[i] - x
        cost += c
        a[i] = a[i] - c
        if a[i] < 0:
            a[i] = 0
print(cost)