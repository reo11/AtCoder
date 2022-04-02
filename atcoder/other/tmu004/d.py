n = int(input())
d = {}
for i in range(n):
    s = input()
    try:
        d[s] += 1
    except:
        d[s] = 1
m = int(input())
for i in range(m):
    s = input()
    try:
        d[s] -= 1
    except:
        d[s] = -1
ans = 0
for v in d.values():
    ans = max(ans, v)
print(ans)
