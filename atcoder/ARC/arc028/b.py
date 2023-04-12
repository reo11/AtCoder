import heapq

n, k = map(int, input().split())
x = list(map(int, input().split()))

ans = []
q = []
for i in range(k):
    q.append([n + 1 - x[i], i + 1])
ans.append(sorted(q)[0][1])
heapq.heapify(q)

for i in range(k, n):
    x_i = n + 1 - x[i]
    min_x, min_idx = heapq.heappop(q)
    heapq.heappush(q, [min_x, min_idx])
    if x_i > min_x:
        # 自分より若い場合のみ入れ替え
        heapq.heappush(q, [x_i, i + 1])
        heapq.heappop(q)
    x_j, idx = heapq.heappop(q)
    heapq.heappush(q, [x_j, idx])
    ans.append(idx)

print("\n".join(list(map(str, ans))))