c = [[] for _ in range(4)]
for i in range(4):
    row = list(map(str, input().split()))
    c[i] = row

l = [[] for _ in range(4)]
for i in range(4):
    for j in range(4):
        l[i].append(c[3 - i][3 - j])
for i in range(4):
    print(" ".join(l[i]))
