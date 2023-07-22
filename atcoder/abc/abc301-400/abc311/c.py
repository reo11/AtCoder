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
    while num <= n:
        if visited[num]:
            num += 1
            continue
        else:
            q.append([num, []])
            num += 1
            break
    while q:
        v, path = q.popleft()
        visited[v] = True
        for u in edges[v]:
            if not visited[u]:
                q.append([u, path + [v]])
            else:
                ans = []
                for ans_v in reversed(path + [v]):
                    ans.append(ans_v)
                    if ans_v == u:
                        ans = ans[::-1]
                        print(len(ans))
                        print(" ".join(map(str, ans)))
                        exit()
