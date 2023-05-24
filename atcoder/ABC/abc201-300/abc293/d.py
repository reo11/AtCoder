import sys
from collections import defaultdict, deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

# 繋げたあとにループ判定を網羅的に行う
graph = defaultdict(lambda: [])

for _ in range(m):
    a, b, c, d = map(str, input().split())
    a = int(a)
    c = int(c)
    graph[a].append(c)
    graph[c].append(a)

used = [False for _ in range(n + 1)]
groups = defaultdict(lambda: [True, set()])

sub_d = deque()
for i in range(1, n + 1):
    sub_d.append(i)
d = deque()
group_id = 1
used_count = 0
# print(graph)
while used_count < n:
    if len(d) > 0:
        current_num, current_group_id = d.popleft()
    else:
        while len(sub_d) > 0:
            i = sub_d.popleft()
            if used[i]:
                continue
            else:
                current_num = i
                break
        current_group_id = group_id
        group_id += 1

    groups[current_group_id][1].add(current_num)
    if not used[current_num]:
        used[current_num] = True
        used_count += 1
        if len(graph[current_num]) != 2:
            groups[current_group_id][0] = False
        for next_num in graph[current_num]:
            if len(graph[next_num]) != 2:
                groups[current_group_id][0] = False
            if not used[next_num]:
                d.append([next_num, current_group_id])

x = 0
y = 0
for is_loop, group_id in groups.values():
    if is_loop:
        x += 1
    else:
        y += 1
print(f"{x} {y}")
