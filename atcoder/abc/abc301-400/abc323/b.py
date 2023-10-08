from collections import defaultdict
n = int(input())
counter = defaultdict(int)
for i in range(n):
    si = list(input())
    for sii in si:
        if sii == "o":
            counter[i + 1] += 1
        else:
            counter[i + 1] += 0

ans = sorted([[v, k] for k, v in counter.items()], key=lambda x: [-x[0], x[1]])
print(*[y for x, y in ans], sep=" ")