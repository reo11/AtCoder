n = int(input())
a = list(map(int, input().split()))

ans = 10 ** 10

# 1 -1 1 -1...
cost1 = 0
s = 0
for i in range(n):
    t = 1 if i % 2 == 0 else -1
    c = 0
    if i % 2 == 0:
        if s + a[i] > 0:
            s += a[i]
        else:
            c = abs(s - t)
            s += c
            cost1 += abs(c - a[i])
    else:
        if s + a[i] < 0:
            s += a[i]
        else:
            c = abs(s - t)
            s -= c
            cost1 += abs(-c - a[i])

cost2 = 0
s = 0
for i in range(n):
    t = -1 if i % 2 == 0 else 1
    c = 0
    if i % 2 == 1:
        if s + a[i] > 0:
            s += a[i]
        else:
            c = abs(s - t)
            s += c
            cost2 += abs(c - a[i])
    else:
        if s + a[i] < 0:
            s += a[i]
        else:
            c = abs(s - t)
            s -= c
            cost2 += abs(-c - a[i])

print(min(cost1, cost2))
# -1 1 -1 1..
