n, k = map(int, input().split())
v = list(map(int, input().split()))
# 再帰関数でいけそうだぞい


def dfs(que, cost, value):
    print(value)
    if cost <= 0:
        return value
    elif len(que) > 1:
        if que[0] < 0:
            tmp1 = max(
                dfs(que[1:], cost - 1, value + que[0]), dfs(que[1:], cost - 2, value)
            )
        else:
            tmp1 = dfs(que[1:], cost - 1, value + que[0])
        if que[-1] < 0:
            tmp2 = max(
                dfs(que[:-1], cost - 1, value + que[-1]), dfs(que[:-1], cost - 2, value)
            )
        else:
            tmp2 = dfs(que[:-1], cost - 1, value + que[-1])
    else:
        tmp1 = value + que[0]
        tmp2 = value + que[-1]
    return max(tmp1, tmp2)


ans = dfs(v, k, 0)
print(ans)
