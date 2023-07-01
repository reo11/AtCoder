n = int(input())
a = list(map(int, input().split()))

ans = [0 for _ in range(n)]
for i in range(n):
    for j in range(7):
        num = i * 7 + j
        ans[i] += a[num]
print(*ans, sep=" ")
