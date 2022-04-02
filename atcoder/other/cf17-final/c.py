n = int(input())
d = list(map(int, input().split()))
d.sort()
ans = min(d)
for i in range(n):
    if i % 2 == 0:
        d[i] = 24 - d[i]

for i in range(n):
    for j in range(n):
        if i != j:
            ans = min(ans, abs(d[i] - d[j]))

print(ans)
