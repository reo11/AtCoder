n = int(input())
abcd = []

for i in range(n):
    a, b, c, d = map(int, input().split())
    abcd.append((a, b, c, d))

grid = [[0] * 101 for _ in range(101)]

for i in range(n):
    a, b, c, d = abcd[i]
    for j in range(a, b):
        for k in range(c, d):
            grid[j][k] = 1

ans = 0
for i in range(101):
    for j in range(101):
        if grid[i][j] == 1:
            ans += 1
print(ans)