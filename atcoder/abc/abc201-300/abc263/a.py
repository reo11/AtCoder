from collections import defaultdict

counter = defaultdict(int)
a = list(map(int, input().split()))
for ai in a:
    counter[ai] += 1

if list(sorted(list(counter.values()))) == [2, 3]:
    print("Yes")
else:
    print("No")
