from collections import defaultdict

s = list(input())
counter = defaultdict(int)

ans = 0
amount = 0
for c in s:
    ans += amount - counter[c]
    amount += 1
    counter[c] += 1

if max(counter.values()) > 1:
    ans += 1

print(ans)