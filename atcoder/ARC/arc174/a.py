import heapq
n, c = map(int, input().split())
a = list(map(int, input().split()))
INF = float('inf')

queue = [[0, 0]]
heapq.heapify(queue)

if c > 0:
    tmp_sum = 0
    ans_lr = [0, -1, -1]
    for i in range(n):
        ai = a[i]
        tmp_sum += ai
        cost, idx = heapq.heappop(queue)
        heapq.heappush(queue, [cost, idx])

        if tmp_sum - cost > ans_lr[0]:
            ans_lr = [tmp_sum - cost, idx, i]
        heapq.heappush(queue, [tmp_sum, i + 1])

    ans = 0
    for i in range(n):
        if ans_lr[1] <= i and i <= ans_lr[2]:
            ans += a[i] * c
        else:
            ans += a[i]
else:
    tmp_sum = 0
    ans_lr = [0, -1, -1]
    for i in range(n):
        ai = a[i]
        tmp_sum += ai
        cost, idx = heapq.heappop(queue)
        cost = -cost
        heapq.heappush(queue, [-cost, idx])

        if tmp_sum - cost < ans_lr[0]:
            ans_lr = [tmp_sum - cost, idx, i]
        heapq.heappush(queue, [-tmp_sum, i + 1])

    ans = 0

    for i in range(n):
        if ans_lr[1] <= i and i <= ans_lr[2]:
            ans += a[i] * c
        else:
            ans += a[i]
print(ans)