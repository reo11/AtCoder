n = int(input())
p = list(map(int, input().split()))
ans = 1

for i in range(1, n):
    ans += i * i

for i in range(1, n):
    if abs(p[i-1] - p[i]) != 1:
        ans -= 1
if abs(p[0] - p[n-1]) != 1:
        ans -= 1

print(ans)