n = int(input())
sa = [list(input().split()) for _ in range(n)]

# 最小を見つける
min_i = [float("inf"), float("inf")]
for i in range(n):
    if min_i[1] > int(sa[i][1]):
        min_i = [i, int(sa[i][1])]

ans = []
for i in range(min_i[0], n):
    ans.append(sa[i][0])

for i in range(min_i[0]):
    ans.append(sa[i][0])
print(*ans, sep="\n")
