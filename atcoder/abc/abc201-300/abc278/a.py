from collections import deque
n, k = map(int, input().split())
a = list(map(int, input().split()))
a = deque(a)

for i in range(k):
    a.popleft()
    a.append(0)
print(*a, sep=" ")
