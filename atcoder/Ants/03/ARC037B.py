from collections import defaultdict

n, m = map(int, input().split())
connected_dict = defaultdict(lambda: [])

for i in range(m):
    u, v = map(int, input().split())
    connected_dict[u].append(v)
    connected_dict[v].append(u)


def dfs(pre_node, node):
    checked_list.append(node)
    l = [True]
    for next_node in connected_dict[node]:
        if next_node == pre_node:
            continue
        if next_node in checked_list:
            return False
        l.append(dfs(node, next_node))
    return all(l)


count = 0
checked_list = []
for node in range(1, n + 1):
    if node not in checked_list:
        if dfs(-1, node):
            count += 1
print(count)
