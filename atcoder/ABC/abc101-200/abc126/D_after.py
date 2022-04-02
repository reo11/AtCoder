import queue

n = int(input())
links = [set() for _ in [0] * n]
for i in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    links[u].add((v, w))
    links[v].add((u, w))
ans = [-1] * n
q = queue.Queue()
q.put((0, 0, -1))
while not q.empty():
    v, d, p = q.get()
    if d % 2 == 0:
        ans[v] = 0
    else:
        ans[v] = 1
    for u, w in links[v]:
        if u == p:
            continue
        q.put((u, d + w, v))
for i in ans:
    print(i)
