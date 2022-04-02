from collections import deque

x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort()
q.sort()
r.sort()

reds = deque(p)
greens = deque(q)
uncolor = deque(r)

for i in range(a + b + c - (x + y)):
    
