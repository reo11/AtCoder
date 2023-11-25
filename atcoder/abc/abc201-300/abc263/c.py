import itertools

n, m = map(int, input().split())

ans = []

for p in itertools.permutations(range(1, m + 1), n):
    flag = True
    for i in range(len(p) - 1):
        if p[i] >= p[i + 1]:
            flag = False
            break
    if flag:
        ans.append(" ".join(list(map(str, p))))
print(*ans, sep="\n")