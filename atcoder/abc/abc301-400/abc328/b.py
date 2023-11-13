n = int(input())
d = list(map(int, input().split()))

ans = 0
for i in range(n):
    m = i + 1
    for j in range(d[i]):
        di = j + 1
        md_set = set(list(str(m)) + list(str(di)))
        if len(md_set) == 1:
            ans += 1
print(ans)