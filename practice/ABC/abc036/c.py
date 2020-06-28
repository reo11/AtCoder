n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

a_l = list(set(a))
a_l.sort()

d = {}

for i, v in enumerate(a_l):
    d[v] = i

out = []
for v in a:
    out.append(str(d[v]))
print("\n".join(out))
