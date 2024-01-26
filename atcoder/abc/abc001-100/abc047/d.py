from collections import defaultdict

n, t = map(int, input().split())
a = list(map(int, input().split()))

ans = defaultdict(int)
min_v = [10**9 + 1, 1]

for v in a:
    ans[v - min_v[0]] += min_v[1]
    if v < min_v[0]:
        min_v = [v, 1]
    elif v == min_v[0]:
        min_v[1] += 1
ans = sorted(ans.items(), key=lambda x: x[0], reverse=True)
print(ans[0][1])
