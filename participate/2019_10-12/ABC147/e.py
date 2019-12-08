h, w = map(int, input().split())
a = [[int(i) for i in input().split()] for i in range(h)]
b = [[int(i) for i in input().split()] for i in range(h)]
ab = []
for i in range(h):
    l = []
    for j in range(w):
        l.append(abs(a[i][j]-b[i][j]))
    ab.append(l)
print(ab)

