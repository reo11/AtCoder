from collections import deque

n = int(input())
a = list(map(int, input().split()))
a = list(set(a))
a.sort()
d = deque(a)

money = n - len(d)
ans = 1
while(len(d) > 0 or len(d) + money >= 2):
    if len(d) > 0 and d[0] == ans:
        d.popleft()
        ans += 1
    elif money >= 2:
        money -= 2
        ans += 1
    elif money == 1 and len(d) >= 1:
        d.pop()
        money -= 1
        ans += 1
    elif len(d) >= 2:
        d.pop()
        d.pop()
        ans += 1
    else:
        break
print(ans - 1)
