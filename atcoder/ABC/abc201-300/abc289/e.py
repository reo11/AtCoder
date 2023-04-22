from collections import defaultdict, deque
t = int(input())

def solve(n, m, c, edges):
    visited = defaultdict(lambda: False)
    visited[1] = True
    q = deque([[1, n, 0]])
    ans = -1
    while len(q) > 0:
        takahashi_current_num, aoki_current_num, cost = q.popleft()
        if current_num == n and aoki_current_num == 1:
            ans = cost
            break
        for next_num in edges[current_num]:
            if visited[next_num]:
                continue
            if colors[current_num] == colors[next_num]:
                continue
            visited[next_num] = True
            q.append([next_num, cost + 1])
    return ans

ans = []
for _ in range(t):
    n, m = map(int, input().split())
    c_l = list(map(int, input().split()))
    colors = dict()
    for i, c_i in enumerate(c_l):
        colors[i + 1] = c_i
    uv = defaultdict(lambda: [])
    for _ in range(m):
        u, v = map(int, input().split())
        uv[u].append(v)
        uv[v].append(u)
    ans.append(str(solve(n, m, colors, uv)))
print("\n".join(ans))