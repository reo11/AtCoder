l = set()
n = int(input())

for x in range(n + 1):
    for y in range(n + 1):
        for z in range(n + 1):
            if x + y + z <= n:
                l.add((x, y, z))
l = list(l)
l.sort()
l = [" ".join(map(str, x)) for x in l]

print(*l, sep="\n")