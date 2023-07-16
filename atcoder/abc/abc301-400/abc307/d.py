from collections import deque

n = int(input())
s = list(input())

# 高さを持っておく
queue = deque([])
delete_range = []

for i in range(n):
    if s[i] == "(":
        queue.append(i)
    elif s[i] == ")":
        if len(queue) > 0:
            pre_i = queue.pop()
            delete_range.append([pre_i, i])

delete_range.sort(key=lambda x: (x[0], -x[1]))
delete_range = deque(delete_range)
imos_list = [0 for _ in range(n + 1)]

for delete_from, delete_until in delete_range:
    imos_list[delete_from] += 1
    imos_list[delete_until + 1] -= 1

v = 0
for i in range(len(imos_list)):
    v += imos_list[i]
    imos_list[i] = v

ans = []
for i in range(n):
    if imos_list[i] == 0:
        ans.append(s[i])

print(*ans, sep="")
