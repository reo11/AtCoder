n, m = map(int, input().split())
a = list(map(int, input().split()))

sums = [0 for _ in range(m)]

for i in range(n):
    xi = list(map(int, input().split()))
    for j in range(m):
        sums[j] += xi[j]

flag = True
for i in range(m):
    if sums[i] < a[i]:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
