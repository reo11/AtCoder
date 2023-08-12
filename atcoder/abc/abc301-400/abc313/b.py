from collections import defaultdict, deque
n, m = map(int, input().split())
ab = defaultdict(lambda: [])
for _ in range(m):
    a, b = map(int, input().split())
    ab[a - 1].append(b - 1)

# 全員を最強として、矛盾が発生したら、その人を最強から外す
# また、その木に関与しない、あるいは別の枝を発生させる人物が存在する場合NG

# 木構造を作る

ans = -1
for i in range(n):
    # 辿っていく
    q = deque([])
    visited = [False] * n
    visited[i] = True
    q.append(i)
    count = 0
    while q:
        now = q.popleft()
        count += 1
        for next in ab[now]:
            if visited[next]:
                continue
            q.append(next)
            visited[next] = True
    if count == n:
        ans = i + 1
        break
print(ans)