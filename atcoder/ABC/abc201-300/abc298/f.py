from collections import defaultdict
n = int(input())

counter_r = defaultdict(int)
counter_c = defaultdict(int)
d = defaultdict(int)
for _ in range(n):
    r, c, x = map(int, input().split())
    d[f"{r}_{c}"] = x
    counter_r[r] += x
    counter_c[c] += x

ans = 0
sorted_r = sorted(counter_r.items(), key=lambda x: -x[1])
sorted_c = sorted(counter_c.items(), key=lambda x: -x[1])
for r, v_r in sorted_r:
    for c, v_c in sorted_c:
        key = f"{r}_{c}"
        if key in d:
            ans = max(ans, v_r + v_c - d[key])
        else:
            ans = max(ans, v_r + v_c)
            break
# print(sorted_c)
# print(sorted_r)
# print(d)
print(ans)