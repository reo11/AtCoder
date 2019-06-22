n = int(input())
l = []
for i in range(n):
    s, p = input().split()
    s = str(s)
    p = int(p)
    l.append([s, p, i+1])
l = sorted(l, key=lambda x: (x[0], -x[1]))
for i in range(n):
    print(l[i][2])
