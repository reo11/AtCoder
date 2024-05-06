n = int(input())
a = [[i for i in list(str(input()))] for _ in range(n)]
b = [[i for i in list(str(input()))] for _ in range(n)]

ans = [-1, -1]

for i in range(n):
    for j in range(n):
        if a[i][j] != b[i][j]:
            ans = [i + 1, j + 1]
            break
    if ans != [-1, -1]:
        break
print(*ans, sep=" ")