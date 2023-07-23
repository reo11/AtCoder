from collections import defaultdict, deque

n = int(input())
a = list(map(int, input().split()))

edges = defaultdict(lambda: [])

for i in range(n):
    edges[i + 1].append(a[i])

visited = [False for _ in range(n + 1)]

q = deque()

num = 1

while num <= n:
    # 探索する頂点を決める
    path = [-1 for _ in range(n + 1)]
    while num <= n:
        if visited[num]:
            num += 1
            continue
        else:
            q.append([num, 0])
            num += 1
            break
    while q:
        v, number = q.popleft()
        path[number] = v
        visited[v] = True
        for u in edges[v]:
            if not visited[u]:
                q.appendleft([u, number + 1])
                visited[u] = True
            else:
                ans = []
                for path_i in reversed(range(number + 1)):
                    ans.append(path[path_i])
                    if path[path_i] == u:
                        ans = ans[::-1]
                        print(len(ans))
                        print(" ".join(map(str, ans)))
                        exit()
