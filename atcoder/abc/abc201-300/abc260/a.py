from collections import defaultdict

s = list(input())
counter = defaultdict(int)
for c in s:
    counter[c] += 1

for k, v in counter.items():
    if v == 1:
        print(k)
        exit()
print(-1)