import heapq
n, q = map(int, input().split())

events = []

ans = []
already_solved = set()
called = []
heapq.heapify(called)
min_a = 1
for _ in range(q):
    event = list(map(int, input().split()))
    if event[0] == 1:
        heapq.heappush(called, min_a)
        min_a += 1
    elif event[0] == 2:
        already_solved.add(event[1])
    else:
        while True:
            a = heapq.heappop(called)
            if a in already_solved:
                continue
            else:
                heapq.heappush(called, a)
                break
        ans.append(str(a))
print("\n".join(ans))