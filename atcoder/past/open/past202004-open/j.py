import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)
s = input()
n = len(s)
ans = ""

que = deque([""])

for i in range(n):
    # print(que)
    if s[i] == "(":
        que.append("")
    elif s[i] == ")":
        v = que.pop()
        if len(que) > 0:
            que[-1] += v + v[::-1]
        else:
            que.append(v + v[::-1])
    else:
        que[-1] += s[i]
print(que[0])
