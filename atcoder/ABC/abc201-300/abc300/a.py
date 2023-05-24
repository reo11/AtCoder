n, a, b = map(int, input().split())
c = list(map(int, input().split()))

ans = 0
for i in range(1, n + 1):
    if a + b == c[i - 1]:
        ans = i
        break
print(ans)
