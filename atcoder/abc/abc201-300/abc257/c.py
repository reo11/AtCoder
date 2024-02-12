from collections import deque

INF = float("inf")
n = int(input())
s = list(map(int, list(input())))
w = list(map(int, input().split()))

count = 0
sw = []
for si, wi in zip(s, w):
    sw.append([wi, si])
    if si:
        count += 1
sw.sort()
sw = deque(sw)

candidates = [0]
for wi in w:
    candidates.append(wi)
candidates = list(set(candidates))
candidates.sort()
candidates.append(INF)

ans = count
for ci in candidates:
    # print(ci, ans, sw)
    while len(sw) > 0 and sw[0][0] <= ci:
        wi, si = sw.popleft()
        if si == 0:
            count += 1
        else:
            count -= 1
    ans = max(ans, count)
print(ans)
