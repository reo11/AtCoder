n = int(input())
a = list(map(int, input().split()))

ans = []

for i in range(n - 1):
    ans.append(a[i] * a[i + 1])
print(*ans, sep=" ")