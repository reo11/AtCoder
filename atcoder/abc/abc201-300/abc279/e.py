n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = []
for i in range(1, m + 1):
    b = list(range(1, n + 1))
    for j in range(1, m + 1):
        if i == j:
            continue
        swap = b[a[j - 1] - 1]
        b[a[j - 1] - 1] = b[a[j - 1]]
        b[a[j - 1]] = swap
    # print(b)
    for j in range(n):
        if b[j] == 1:
            ans.append(j + 1)
            break
print(*ans, sep="\n")
