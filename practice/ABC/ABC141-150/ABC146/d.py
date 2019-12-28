from collections import defaultdict
n = int(input())
ab = [list(map(int, input())) for _ in range(n)]

count = [0] * (n+1)
for a, b in ab:
    count[a] += 1; count[b] += 1

max_ = 0
max_num = 0
for i in range(n+1):
    if max_ < count[i]:
        max_num = i
        max_ = count[i]

d = defaultdict(lambda: [])
places = defaultdict(lambda: defaultdict(lambda: -1))
color = defaultdict(lambda: defaultdict(lambda: -1))

for i, (a, b) in enumerate(ab):
    d[a].append(b)
    d[b].append(a)
    places[a][b] = i
    places[b][a] = i

ans = []


ans.append(ab[0])
a, b = ab[0]

def dfs(cur):
    for next_ in d[cur]:
        if color[cur][next_] == -1 and color[next_][cur] == -1:
            
            dfs(next_)

