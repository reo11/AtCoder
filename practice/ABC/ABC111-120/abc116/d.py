import sys
input = sys.stdin.readline

n, k =map(int, input().split())
td = [list(map(int, input().split())) for _ in range(n)]
td.sort(key=lambda x: x[1], reverse=True)

base = []; other = []
val = set()
yum = 0
for t, d in td[:k]:
    yum += d
    if t in val:
        other.append(d)
    val.add(t)
other.sort(reverse=True)

kouho = []
val_tmp = val.copy()
for t, d in td[k:]:
    if t not in val_tmp:
        kouho.append(d)
        val_tmp.add(t)
kouho.sort()

v = len(val)
ans = yum + (v*v)


while len(other) > 0 and len(kouho) > 0:
    yum -= other.pop()
    yum += kouho.pop()
    v += 1
    ans = max(ans, yum+(v*v))
print(ans)

