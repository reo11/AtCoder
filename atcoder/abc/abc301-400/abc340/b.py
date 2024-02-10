q = int(input())
a = []

ans = []
for i in range(q):
    q_type, x = map(int, input().split())
    if q_type == 1:
        a.append(x)
    else:
        ans.append(a[-x])
print(*ans, sep="\n")