from collections import deque

n = int(input())
x = list(map(int, input().split()))
x.sort()
x = deque(x)

for i in range(n):
    x.pop()
    x.popleft()
print(sum(x) / len(x))
