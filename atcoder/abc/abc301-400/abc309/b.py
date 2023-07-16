n = int(input())
a = []
b = []
for _ in range(n):
    a_i = list(input())
    a.append(a_i[:])
    b.append(a_i[:])

current = (0, 1)
pre_value = a[0][0]
d = (0, 1)
while True:
    x, y = current
    b[x][y] = pre_value
    if d == (0, 1) and y == n - 1:
        d = (1, 0)
    if d == (1, 0) and x == n - 1:
        d = (0, -1)
    if d == (0, -1) and y == 0:
        d = (-1, 0)
    current = (x + d[0], y + d[1])
    pre_value = a[x][y]
    if current == (0, 0):
        b[0][0] = pre_value
        break

ans = []
for i in range(n):
    ans.append("".join(map(str, b[i])))
print(*ans, sep="\n")
