n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

ans = []
for i in range(n):
    ansi = []
    for j in range(n):
        if i == j:
            continue
        if a[i][j] == 1:
            ansi.append(j + 1)
    ans.append(" ".join(list(map(str, ansi))))

print("\n".join(ans))
