from collections import deque
import sys
input = sys.stdin.readline

s = str(input().rstrip())
ans = deque(list(s))

f = True
q = int(input())
for i in range(q):
    q = list(map(str, input().split()))
    if int(q[0]) == 1:
        if f:
            f = False
        else:
            f = True
    else:
        f_i = int(q[1])
        if f_i == 1:
            if f:
                ans.appendleft(q[2])
            else:
                ans.append(q[2])
        else:
            if f:
                ans.append(q[2])
            else:
                ans.appendleft(q[2])
ans = list(ans)
if f:
    print("".join(ans))
else:
    print("".join(ans[::-1]))