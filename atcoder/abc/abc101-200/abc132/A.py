from collections import defaultdict

d = defaultdict(int)
s = list(input())

for c in s:
    d[c] += 1

flag = False

if len(d.keys()) == 2:
    for v in d.values():
        if v != 2:
            flag = False
            break
        else:
            flag = True
if flag:
    print("Yes")
else:
    print("No")
