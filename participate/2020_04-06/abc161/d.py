import sys
sys.setrecursionlimit(20000000)
k = int(input())

def dfs(l, lim):
    if lim == 10:
        return l
    new_l = []
    for num in l:
        last = num % 10
        base = num * 10
        if 1 <= last <= 8:
            for i in [last-1, last, last+1]:
                if base + i <= 3234566667:
                    new_l.append(base + i)
        elif last == 0:
            for i in [0, 1]:
                if base + i <= 3234566667:
                    new_l.append(base + i)
        else:
            for i in [8, 9]:
                if base + i <= 3234566667:
                    new_l.append(base + i)
    return l + new_l + dfs(new_l, lim+1)

ans = list(set(dfs([1, 2, 3, 4, 5, 6, 7, 8, 9], 0)))
ans.sort()

print(ans[k-1])
