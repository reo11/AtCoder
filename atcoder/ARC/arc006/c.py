n = int(input())
w = [int(input()) for _ in range(n)]
INF = 10 ** 12
# 山の数を1～Nで全探索する
ans = INF


def check(v, hako):
    kouho = []
    for i, c in enumerate(hako):
        if v <= c:
            kouho.append((c, i))
    if len(kouho) == 0:
        return -1
    kouho.sort(key=lambda x: (x[0], x[1]))
    return kouho[0][1]


cnt = 0
for i in range(1, n + 1):
    f = True
    hako = [INF for _ in range(i)]
    que = w[::-1]
    while len(que) > 0:
        v = que.pop()
        idx = check(v, hako)
        if idx == -1:
            f = False
            break
        else:
            hako[idx] = v
    if f:
        ans = min(ans, len(hako))
print(ans)
