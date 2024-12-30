from collections import defaultdict
n = int(input())

counter = defaultdict(int)
for _ in range(n):
    s = input()
    counter[s] += 1

print(counter["Takahashi"])
