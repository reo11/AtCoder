n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

data = []

for i in range(n):
    data.append([a[i], b[i], a[i] + b[i], i + 1])

ans = []

data.sort(key=lambda x: [x[0], -x[3]])
for _ in range(x):
    _, _, _, i = data.pop()
    ans.append(i)

data.sort(key=lambda x: [x[1], -x[3]])
for _ in range(y):
    _, _, _, i = data.pop()
    ans.append(i)

data.sort(key=lambda x: [x[2], -x[3]])
for _ in range(z):
    _, _, _, i = data.pop()
    ans.append(i)
ans.sort()
print(*ans, sep="\n")
