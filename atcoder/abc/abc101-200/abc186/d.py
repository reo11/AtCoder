n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = 0

# ai
for i in range(1, n + 1):
    ans += (n - i) * a[i - 1]

# -aj
for i in range(1, n + 1):
    ans -= (i - 1) * a[i - 1]
print(ans)
