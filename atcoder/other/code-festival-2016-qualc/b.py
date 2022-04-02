from heapq import heapify, heappop, heappush

k, t = map(int, input().split())
a = list(map(int, input().split()))

que = []
heapify(que)

for i in range(t):
    heappush(que, (-a[i], i))

s = [-1]
while len(que) > 0:
    if len(que) == 1:
        a_i, idx = heappop(que)
        for _ in range(-a_i):
            s.append(idx)
        break
    else:
        a_i, idx_i = heappop(que)
        if s[-1] == idx_i:
            a_j, idx_j = heappop(que)
            s.append(idx_j)
            heappush(que, (a_i, idx_i))
            a_j += 1
            if a_j < 0:
                heappush(que, (a_j, idx_j))
        else:
            s.append(idx_i)
            a_i += 1
            if a_i < 0:
                heappush(que, (a_i, idx_i))

cnt = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        cnt += 1
print(cnt)
