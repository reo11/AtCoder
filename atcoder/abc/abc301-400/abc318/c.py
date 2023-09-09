from collections import deque
n, d, p = map(int, input().split())
f = list(map(int, input().split()))
f_origin = f[:]
INF = float('inf')
f.sort(reverse=True)
f = deque(f)


ticket_num = 0
while f:
    tmp = []
    sum_tmp = 0
    while f and len(tmp) < d:
        tmp.append(f.popleft())
        sum_tmp += tmp[-1]
    if sum_tmp > p:
        ticket_num += 1

f_origin.sort(reverse=True)
ans = 0
ans += ticket_num * p
for i in range(ticket_num * d, n):
    ans += f_origin[i]
print(ans)
