from collections import defaultdict
n = int(input())
INF = float("inf")

min_counter = defaultdict(lambda: INF)
ac = []
for i in range(n):
    a, c = map(int, input().split())
    min_counter[c] = min(min_counter[c], a)

ans = 0
for v in min_counter.values():
    if v != INF:
        ans = max(ans, v)
print(ans)
