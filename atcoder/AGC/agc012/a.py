n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
ans = 0
for i in range(n):
    ans += a[i * 2 + 1]
print(ans)
