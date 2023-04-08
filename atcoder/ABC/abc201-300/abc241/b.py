n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

from collections import defaultdict

d = defaultdict(lambda: 0)

for a_i in a:
    d[a_i] += 1

flag = True
for b_i in b:
    if d[b_i] > 0:
        d[b_i] -= 1
    else:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
