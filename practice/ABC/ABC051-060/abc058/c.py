from collections import defaultdict

n = int(input())
s = []
for i in range(n):
    s.append(list(str(input())))

alphabet = set(s[0])

for i in range(1, n):
    alphabet = alphabet & set(s[i])

count_min = defaultdict(lambda: 10**9)
for a in sorted(alphabet):
    for i in range(n):
        count_min[a] = min(count_min[a], s[i].count(a))

ans = ""

for k, v in sorted(count_min.items()):
    for i in range(v):
        ans += k
print(ans)