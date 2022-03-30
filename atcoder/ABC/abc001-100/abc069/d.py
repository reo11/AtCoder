h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

c = [[0 for _ in range(w)] for _ in range(h)]
s = []
for i in range(len(a)):
    for j in range(a[i]):
        s.append(i+1)

idx = 0
for i in range(h):
    if i % 2 == 0:
        for j in range(w):
            c[i][j] = s[idx]
            idx += 1
    else:
        for j in reversed(range(w)):
            c[i][j] = s[idx]
            idx += 1

for i in range(len(c)):
    print(" ".join(list(map(str, c[i]))))


