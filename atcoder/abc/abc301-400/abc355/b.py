n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = []

for ai in a:
    c.append([ai, "a"])
for bi in b:
    c.append([bi, "b"])

c.sort()

ans = False
for i in range(1, len(c)):
    if c[i][1] == c[i - 1][1] and c[i][1] == "a":
        ans = True
        break
if ans:
    print("Yes")
else:
    print("No")
