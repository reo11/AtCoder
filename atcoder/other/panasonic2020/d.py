import sys

sys.setrecursionlimit(20000000)
n = int(input())


def dfs(num, l_):
    if num == 0:
        return l_
    l_new = []
    for s, set_size in l_:
        for i in range(set_size + 1):
            s_size = set_size if i < set_size else set_size + 1
            l_new.append((s + chr(ord("a") + i), s_size))
    return dfs(num - 1, l_new)


ans = dfs(n - 1, [("a", 1)])
ans = list(map(lambda x: x[0], ans))
ans.sort()
print("\n".join(ans))
