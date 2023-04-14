import pprint
n = int(input())
status = []
for i in range(n):
    l = list(map(int, input().split()))
    status.append([min(l), i, l])

status.sort(key=lambda x: -x[0])
ans = []
ans.append(status[0])
status.sort(key=lambda x: x[1])

def calc_score(l1, l2, l3):
    maxes = [0 for _ in range(5)]
    for i in range(5):
        maxes[i] = maxes

l1 = ans[0]
for i in range(n):
    if i == ans[0][1]:
        continue
    l2 = status[i]
    for j in range(n):
        if i == j or j == ans[0][1]:
            continue
        l3 = status[j]


# 候補1は確定
ans = float('inf')
max_values = [0 for _ in range(5)]

for i in range(3):
    min_v, l = status[i]
    for i, st in enumerate(l):
        max_values[i] = max(max_values[i], st)
ans = min(max_values)
pprint.pprint(status)
print(ans)
