from collections import deque

q = int(input())
queries = []

for _ in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

q = deque([])
current_pos = 0
last_pos = 0
ans = []
for query in queries:
    if query[0] == 1:
        _, x, c = query
        # xをc個追加
        if len(q) > 0:
            last_pos = q[-1][0]
        q.append([last_pos + c, x])
    else:
        _, c = query
        ansi = 0
        end = current_pos + c
        while current_pos < end:
            if len(q) == 0:
                break
            pos, x = q.popleft()
            if pos < end:
                ansi += x * (pos - current_pos)
                current_pos = pos
            else:
                ansi += x * (end - current_pos)
                current_pos = end
                q.appendleft([pos, x])
                break
        ans.append(ansi)
print(*ans, sep="\n")
