n = int(input())
a = list(map(int, input().split()))

idx = 1
for i in range(n):
    if a[i] == idx:
        idx += 1
if idx == 1:
    print(-1)
else:
    print(n - idx + 1)
