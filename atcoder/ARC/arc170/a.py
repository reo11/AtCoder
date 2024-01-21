from collections import deque
INF = float('inf')
n = int(input())
s = list(input())
t = list(input())

ans = 0
queue_a = deque()
queue_b = deque()

for i, (si, ti) in enumerate(zip(s, t)):
    if si != ti:
        if si == 'A':
            queue_a.append(i)
        else:
            queue_b.append(i)
s = [[si, 0] for si in s]

# print(queue_a, queue_b)
single_a = []
while queue_a and queue_b:
    if queue_b[0] < queue_a[0]:
        xb = queue_b.popleft()
        xa = queue_a.popleft()
        s[xb][0] = "A"
        s[xb][1] = 1
        s[xa][0] = "B"
        s[xa][1] = 1
        ans += 1
    elif queue_b[0] > queue_a[0]:
        x = queue_a.popleft()
        single_a.append(x)

for i in single_a:
    s[i][1] = -1
for i in queue_b:
    s[i][1] = -1
for i in queue_a:
    s[i][1] = -1

# print(s)
status_a = False
for i in range(len(s)):
    if status_a == False and (s[i][0] == "A" or s[i][1] == 1):
        status_a = True
    elif s[i][0] == "A" and s[i][1] == -1:
        if status_a:
            ans += 1
            s[i][0] = "B"
            s[i][1] = 1
        else:
            ans = INF
            break

status_b = False
for i in reversed(range(len(s))):
    if status_b == False and (s[i][0] == "B" or s[i][1] == 1):
        status_b = True
    elif s[i][0] == "B" and s[i][1] == -1:
        if status_b:
            ans += 1
            s[i][0] = "A"
            s[i][1] = 1
        else:
            ans = INF
            break

for si, xi in s:
    if xi == -1:
        ans = INF
        break

if ans == INF:
    print(-1)
else:
    print(ans)