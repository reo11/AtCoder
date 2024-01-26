from collections import defaultdict, deque

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# グラフで解く

nodes = defaultdict(lambda: [])
node_num = defaultdict(lambda: -1)
not_processed = deque(list(range(1, n + 1)))
process_queue = deque([])

for i in range(m):
    ai, bi = a[i], b[i]
    nodes[ai].append(bi)
    nodes[bi].append(ai)

while not_processed or process_queue:
    while len(process_queue) == 0 and not_processed:
        node = not_processed.popleft()
        if node_num[node] == -1:
            node_num[node] = 0
            process_queue.append(node)
            break
        else:
            continue

    if len(process_queue) == 0:
        break
    i = process_queue.popleft()
    num = node_num[i]
    if num == -1:
        num = 0
    next_num = (num + 1) % 2
    # print(i, next_num, not_processed, process_queue, node_num)

    for j in nodes[i]:
        if node_num[j] == -1:
            node_num[j] = next_num
            process_queue.appendleft(j)
        elif node_num[j] != next_num:
            print("No")
            exit()
print("Yes")
