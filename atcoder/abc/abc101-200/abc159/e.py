h, w, k = map(int, input().split())
s = [[i for i in list(map(int, list(input())))] for i in range(h)]


def solve(l):
    choco = [0 for _ in range(len(l))]
    ans = 0
    for i in range(w):
        f = True
        tmp = [0 for _ in range(len(l))]
        for idx, vs in enumerate(l):
            for v in vs:
                if s[v][i]:
                    tmp[idx] += 1
        for j in range(len(l)):
            if choco[j] + tmp[j] > k:
                f = False
        if not f:
            ans += 1
            choco = [0 for _ in range(len(l))]
        for idx, vs in enumerate(l):
            for v in vs:
                if s[v][i]:
                    if choco[idx] + 1 > k:
                        return 10 ** 9
                    choco[idx] += 1
    return ans + len(l) - 1


ans = 10 ** 9
for i in range(2 ** (h - 1)):
    div = []
    tmp = []
    for j in range(h):
        tmp.append(j)
        if (i >> j) & 1:
            div.append(tmp)
            tmp = []
    div.append(tmp)
    res = solve(div)
    ans = min(ans, res)
print(ans)
