from collections import deque
x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort(reverse=True)
p = p[:x]
q.sort(reverse=True)
q = q[:y]
r.sort(reverse=True)
apples = p + q + r
apples.sort(reverse=True)
ans = sum(apples[:x+y])

print(ans)
