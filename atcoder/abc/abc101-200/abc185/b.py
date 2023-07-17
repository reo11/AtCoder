n, m, t = map(int, input().split())
ab = []
for _ in range(m):
    a, b = map(int, input().split())
    ab.append([a, b])
status = [0, n]
ans = True
for a, b in ab:
    status[1] = status[1] - (a - status[0])
    if status[1] <= 0:
        ans = False
        break
    status[0] = b
    status[1] = min(n, status[1] + (b - a))

if status[1] - (t - status[0]) <= 0:
    ans = False

print(["No", "Yes"][ans])
