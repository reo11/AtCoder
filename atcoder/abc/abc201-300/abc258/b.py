n = int(input())
a = [list(input()) for _ in range(n)]

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]

ans = []

for start_i in range(n):
    for start_j in range(n):
        for dx, dy in dxy:
            ansi = []
            for i in range(n):
                ni, nj = (start_i + i * dx) % n, (start_j + i * dy) % n
                ansi.append(a[ni][nj])
            ans.append(int("".join(ansi)))
print(max(ans))
