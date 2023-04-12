from collections import deque
l, n1, n2 = map(int, input().split())
x1 = deque()
x2 = deque()

for _ in range(n1):
    v, l = map(int, input().split())
    x1.append([v, l])

for _ in range(n2):
    v, l = map(int, input().split())
    x2.append([v, l])

# 1, 2でそれぞれindexを格納し、更新していくとO(N1 + N2)

idx1 = [0, -1]
idx2 = [0, -2]
ans = 0
while len(x1) > 0 or len(x2) > 0:
    if idx1[0] > idx2[0] or len(x1) == 0:
        pre_idx = idx2[0]
        l, v = x2.popleft()
        if idx1[1] == l:
            ans += min(idx1[0], pre_idx + v) - pre_idx
        idx2 = [pre_idx + v, l]
    else:
        pre_idx = idx1[0]
        l, v = x1.popleft()
        if idx2[1] == l:
            ans += min(idx2[0], pre_idx + v) - pre_idx
        idx1 = [pre_idx + v, l]
print(ans)