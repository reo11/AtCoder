n = int(input())
p = list(map(int, input().split()))

ans = []
for i in range(n):
    min_d = float("inf")
    for j in range(n):
        if i == j:
            continue
        min_d = min(min_d, abs(p[i] - p[j]) + abs((i + 1) - (j + 1)))
    ans.append(min_d)
print(*ans, sep=" ")
