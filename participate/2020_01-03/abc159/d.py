from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for v in a:
    d[v] += 1

max_ans = 0
for k, v in d.items():
    max_ans += v * (v-1) // 2

ans = []
for v in a:
    if d[v] > 1:
        ans.append(max_ans - ((d[v]) * (d[v]-1) // 2) + ((d[v]-1) * (d[v]-2) // 2))
    else:
        ans.append(max_ans)

print("\n".join(list(map(str, ans))))