n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if i == a[a[i] - 1] - 1:
        cnt += 1
print(cnt // 2)