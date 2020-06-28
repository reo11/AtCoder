n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
right = 0
for i in range(n):
    if b[i] >= a[i] + a[i+1]:
        ans += a[i] + a[i+1]
        a[i] = 0
        a[i+1] = 0
    elif b[i] <= a[i]:
        ans += b[i]
        a[i] = a[i] - b[i]
    else: # b[i] < a[i] + a[i+1]
        ans += b[i]
        a[i+1] = a[i+1] - (b[i] - a[i])
        a[i] = 0
print(ans)
        