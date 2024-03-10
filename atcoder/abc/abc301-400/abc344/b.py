from collections import deque
ans = deque()
for i in range(100):
    ai = int(input())
    ans.appendleft(ai)
    if ai == 0:
        break
print(*ans, sep="\n")
