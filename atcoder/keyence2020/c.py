n, k, s = map(int, input().split())
a = []
for i in range(k):
    a.append(s)
if s > 10**8:
    for i in range(n - k):
        a.append(1)
else:
    for i in range(n - k):
        a.append(10**9)
a = list(map(str, a))
print(" ".join(a))