from collections import defaultdict

N, M = map(int, input().split())
X = defaultdict(lambda: set())
for _ in range(M):
    x = list(map(int, input().split()))
    for x_i in x[1:]:
        for x_j in x[1:]:
            if x_i == x_j:
                continue
            X[x_i].add(x_j)

flag = True

for x_i in range(1, N + 1):
    for x_j in range(1, N + 1):
        if x_i == x_j:
            continue
        if x_j not in X[x_i]:
            flag = False

if flag:
    print("Yes")
else:
    print("No")
