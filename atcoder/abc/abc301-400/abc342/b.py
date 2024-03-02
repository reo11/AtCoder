from collections import defaultdict

n = int(input())
p_map = defaultdict(lambda: -1)
p = list(map(int, input().split()))
for i in range(n):
    p_map[p[i]] = i + 1

q = int(input())
ans = []
for _ in range(q):
    a, b = map(int, input().split())
    if p_map[a] < p_map[b]:
        ans.append(a)
    else:
        ans.append(b)

print(*ans, sep="\n")
