from collections import deque

ans = set()
s = list(input())
n = len(s)

for i in range(n):
    for j in range(i + 1, n + 1):
        ans.add("".join(s[i:j]))

print(len(ans))

