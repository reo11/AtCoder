from collections import Counter

n = int(input())

x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())

l_ = []
for i in range(n):
    pre = [x[i], y[i]]
    for j in range(n):
        if i == j:
            continue
        l_.append("{}_{}".format(x[j] - pre[0], y[j] - pre[1]))

if len(l_) > 0:
    c = Counter(l_)
    a = int(c.most_common()[0][1])
    print(n - a)
else:
    print(1)
