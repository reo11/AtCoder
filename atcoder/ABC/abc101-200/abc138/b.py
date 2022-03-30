n = int(input())
a = list(map(int, input().split()))
ans = 0
b = 0
for i in range(n):
    b += 1 / a[i]
ans = 1 / b
print(ans)