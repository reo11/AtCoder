from collections import Counter
n = int(input())

x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())

l = []
pre = [-10**9, -10**9]
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        l.append("{}_{}".format(x[i] - pre[0], y[i] - pre[1]))
    pre = [x[i], y[i]]

if len(l) > 0:
    c = Counter(l)
    min_cost = 10**9
    for idx in range(len(c)):
        p, q = map(int, c.most_common()[idx][0].split("_"))

        cost = 1
        pre = [x[0], y[0]]
        for i in range(1, n):
            if not(pre[0] == x[i] - p and pre[1] == y[i] - q):
                cost += 1
            pre = [x[i], y[i]]
        min_cost = min(cost, min_cost)
    print(min_cost)
else:
    print(1)
