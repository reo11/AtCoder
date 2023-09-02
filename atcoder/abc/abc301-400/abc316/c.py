from collections import defaultdict, deque
n, m = map(int, input().split())
abc = []

roads = defaultdict(lambda: [])
for _ in range(m):
    a, b, c = map(int, input().split())
    abc.append((a, b, c))
    roads[a - 1].append([b - 1, c])
    roads[b - 1].append([a - 1, c])

ans = 0
for start_from in range(n):
    # 距離の最大値を求める
    # 深さ優先探索っぽいことをする
    visited = set()
    path = deque()
    q = deque([[start_from, 0, 1]])
    while q:
        now, dist, path_num = q.popleft()
        while len(path) >= path_num:
            deleted = path.pop()
            visited.discard(deleted)
        if now in visited:
            continue
        path.append(now)
        visited.add(now)

        ans = max(ans, dist)
        # print(start_from, path, q, ans)
        for next, next_dist in roads[now]:
            if next in visited:
                continue
            q.appendleft([next, dist + next_dist, path_num + 1])
print(ans)