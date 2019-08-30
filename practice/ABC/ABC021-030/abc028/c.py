import itertools

ans = []
seq = list(map(int, input().split()))
for vs in list(itertools.combinations(seq,3)):
    s = 0
    for v in vs:
        s += v
    ans.append(s)
ans.sort(reverse=True)
print(ans[2])