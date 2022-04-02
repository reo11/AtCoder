a = int(input())
ans = 0
for x in range(a + 1):
    y = a - x
    ans = max(ans, x * y)
print(ans)
