n, a, b = map(int, input().split())
d = list(map(int, input().split()))

mods = set()
INF = float("inf")
for di in d:
    mods.add(di % (a + b))

mods = list(sorted(mods))

if max(mods) - min(mods) < a:
    print("Yes")
    exit()
for i in range(len(mods) - 1):
    max1 = mods[i]
    min2 = mods[i + 1]
    if max1 + (a + b - min2) < a:
        print("Yes")
        exit()
print("No")
