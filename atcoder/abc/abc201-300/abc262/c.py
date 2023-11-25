n = int(input())
a = list(map(int, input().split()))
ans = 0
count = 0
for i in range(n):
    ai = a[i] - 1
    if i < ai:
        if a[ai] == i + 1:
            ans += 1
    elif i == ai:
        count += 1

if count > 0:
    ans += count * (count - 1) // 2
print(ans)