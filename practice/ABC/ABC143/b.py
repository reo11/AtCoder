n = int(input())
d = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        ans += d[i] * d[j]
print(ans//2)