from collections import deque
s = list(input())
# Aで下げる
q = deque([])
for si in s:
    q.appendleft(si)
    if len(q) >= 3:
        if q[0] == "C" and q[1] == "B" and q[2] == "A":
            q.popleft()
            q.popleft()
            q.popleft()
        else:
            continue
    else:
        continue
ans = reversed(list(q))
print("".join(ans))
