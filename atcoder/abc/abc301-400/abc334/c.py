from collections import deque
INF = float('inf')
n, k = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)

a_prefix = [0]
a_suffix = [0]

tmp_a = a[:]
tmp_a = deque(tmp_a)
while len(tmp_a) > 1:
    x = tmp_a.popleft()
    y = tmp_a.popleft()
    v = a_prefix[-1] + abs(x - y)
    a_prefix.append(v)
    a_prefix.append(v)

tmp_a = a[:]
tmp_a = reversed(tmp_a)
tmp_a = deque(tmp_a)
while len(tmp_a) > 1:
    x = tmp_a.popleft()
    y = tmp_a.popleft()
    v = a_suffix[-1] + abs(x - y)
    a_suffix.append(v)
    a_suffix.append(v)
a_suffix = list(reversed(a_suffix))
ans = 0
if k % 2 == 0:
    while a:
        x = a.pop()
        y = a.pop()
        ans += abs(x - y)
elif k == 1:
    ans = 0
else:
    ans = INF
    for i in range(k):
        tmp_ans = 0
        tmp_ans = a_prefix[i] + a_suffix[i]
        ans = min(ans, tmp_ans)
# print(a_prefix, a_suffix)
print(ans)