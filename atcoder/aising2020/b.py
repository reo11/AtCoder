n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in range(1, n + 1):
    if i % 2 and a[i - 1] % 2:
        cnt += 1
print(cnt)
