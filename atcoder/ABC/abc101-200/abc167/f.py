import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)


def remove(s):
    n = len(s)
    que = deque([""])
    for i in range(n):
        if que[-1] == "(" and s[i] == ")":
            que.pop()
        else:
            que.append(s[i])
    return "".join(que)


n = int(input())

s = [[], [], []]
for i in range(n):
    s_ = remove(input())
    t1 = s_.count("(")
    t2 = s_.count(")")
    if t1 > 0 and t2 > 0:
        s[1].append(s_)
    elif t1 > 0:
        s[0].append(s_)
    else:
        s[2].append(s_)

s[0] = sorted(s[0])
s[1] = sorted(s[1])
s[2] = sorted(s[2])
for i in range(3):
    s[i] = "".join(s[i])

s = "".join(s)
s = remove(s)
if len(s) == 0:
    print("Yes")
else:
    print("No")
