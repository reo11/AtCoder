n, q = map(int, input().split())

a = [str(0)] * n

for i in range(q):
    l, r, t = map(int, input().split())
    l -= 1
    for i in range(l, r):
        a[i] = str(t)
print("\n".join(a))
