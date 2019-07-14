import queue
import random

q = queue.Queue()
n, m = map(int, input().split())
ab = [[] for _ in range(n + 1)]
count = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    if random.random() < 0.5:
        tmp = a
        a = b
        b = tmp
    ab[a].append((a, b))
    ab[b].append((a, b))
    count[a] += 1

for i in range(1, n+1):
    if count[i] % 2 == 1:
        q.put(i)

if m % 2 == 1:
    print(-1)
else:
    while not q.empty():
        i = q.get()
        if count[i] % 2 == 0:
            continue
        (a, b) = random.choice(ab[i])
        ab[i].remove((a, b))
        count[a] -= 1
        count[b] += 1
        ab[i].append((b, a))
        if a != i:
            ab[a].remove((a, b))
            ab[a].append((b, a))
            if count[a] % 2 == 1:
                q.put(a)
        else:
            ab[b].remove((a, b))
            ab[b].append((b, a))
            if count[b] % 2 == 1:
                q.put(b)
    ans = set()
    for l in ab:
        for (a, b) in l:
            ans.add((a, b))
    ans_str = []
    for (a, b) in ans:
        ans_str.append(str(a) + " " +  str(b))
    print("\n".join(ans_str))
