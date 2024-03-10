from collections import defaultdict

INF = float("inf")
t = input()
n = int(input())

ass = []
for i in range(n):
    ai, *si = input().split()
    ass.append(si)

min_visited = defaultdict(lambda: INF)
min_visited[""] = 0

current_queue = [["", 0]]
for i in range(n):
    next_queue = []
    for prefix, cost in current_queue:
        for j in range(len(ass[i])):
            tmp_str = prefix + ass[i][j]
            if len(tmp_str) <= len(t) and tmp_str == t[:len(tmp_str)]:
                if i < n - 1 or (i == n - 1 and tmp_str == t):
                    if min_visited[tmp_str] > cost + 1:
                        next_queue.append([tmp_str, cost + 1])
                        min_visited[tmp_str] = cost + 1
        if i < n - 1 or (i == n - 1 and prefix == t):
            if min_visited[prefix] >= cost:
                next_queue.append([prefix, cost])
                min_visited[prefix] = cost
    current_queue = next_queue

if len(current_queue) == 0:
    ans = -1
else:
    ans = min([x for _, x in current_queue])

print(ans)