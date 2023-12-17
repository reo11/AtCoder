n = int(input())

candidates = []
for i in range(1, 14):
    si = ""
    for j in range(i):
        si += "1"
    candidates.append(int(si))

candidates.sort()

ans = set()
max_prosess = 13
for i in range(max_prosess):
    for j in range(i, max_prosess):
        for k in range(j, max_prosess):
            ans.add(candidates[i] + candidates[j] + candidates[k])
ans = list(ans)
ans.sort()

print(ans[n - 1])
