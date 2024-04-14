from collections import defaultdict

counter = defaultdict(int)

s = list(input())

for si in s:
    counter[si] += 1

valid_counter = defaultdict(lambda: set())
for k, v in counter.items():
    valid_counter[v].add(k)

flag = True
for k, v in valid_counter.items():
    if len(v) == 0 or len(v) == 2:
        continue
    else:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
