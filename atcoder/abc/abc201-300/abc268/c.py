from collections import defaultdict
n = int(input())
p = list(map(int, input().split()))

counter = defaultdict(int)
for i in range(n):
    pi = p[i]
    spins = []

    for j in range(3):
            spins.append((n + (pi - i - 1 + j)) % n)
    for s in spins:
        counter[s] += 1

print(max(counter.values()))
