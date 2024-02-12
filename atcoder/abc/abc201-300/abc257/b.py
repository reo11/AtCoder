positions = dict()
n, k, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

flags = [False for _ in range(n + 1)]

for i, ai in enumerate(a, start=1):
    flags[ai] = True
    positions[i] = ai

for li in l:
    pos = positions[li]
    if pos == n:
        continue
    else:
        if not flags[pos + 1] and flags[pos]:
            flags[pos] = False
            flags[pos + 1] = True
            positions[li] = pos + 1

ans = []
for i in range(1, n + 1):
    if flags[i]:
        ans.append(i)
print(*ans, sep=" ")