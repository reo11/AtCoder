import heapq

n, m = map(int, input().split())

events = []
heapq.heapify(events)

for _ in range(m):
    t, w, s = map(int, input().split())
    # イベントをスケジュールに追加
    heapq.heappush(events, [t, 0, w, s])


# イベントを順に処理
ans = [0 for _ in range(n)]
people_queue = list(range(n))
heapq.heapify(people_queue)

while events:
    t, event_type, w, s = heapq.heappop(events)
    if event_type == 0:
        # そうめんを流す
        if len(people_queue) == 0:
            continue
        target_num = heapq.heappop(people_queue)
        ans[target_num] += w
        heapq.heappush(events, [t + s - 0.5, 1, target_num, -1])
    else:
        # 人を復活させる
        heapq.heappush(people_queue, w)
print(*ans, sep="\n")
