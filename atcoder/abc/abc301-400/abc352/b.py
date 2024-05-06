from collections import deque
s = list(input())
t = list(input())

s = deque(s)
t = deque(t)

n = len(t)
cnt = 1
ans = []
while len(s) > 0 and len(t) > 0:
    if s[0] == t[0]:
        s.popleft()
        t.popleft()
        ans.append(cnt)
    else:
        t.popleft()
    cnt += 1
ans = sorted(ans)
print(*ans, sep=" ")