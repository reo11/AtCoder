import bisect

INF = 10 ** 15
n, W = map(int, input().split())
w = []
v = []
max_w = 0
max_v = 0
for i in range(n):
    v_, w_ = map(int, input().split())
    if max_v < v_:
        max_v = v_
    if max_w < w_:
        max_w = w_
    w.append(w_)
    v.append(v_)

# N <= 30
def solve1():
    global n, W, items
    # 半分全列挙
    a = n // 2
    b = n - a

    items1 = []
    items2 = []
    for i in range(2 ** a):
        w_ = 0
        v_ = 0
        for j in range(a):
            if i & 2 ** j > 0:
                w_ += w[j]
                v_ += v[j]
        items1.append([w_, v_])
    items1 = sorted(items1, key=lambda x: (x[0], -x[1]))
    for i in range(2 ** b):
        w_ = 0
        v_ = 0
        for j in range(b):
            if i & 2 ** j > 0:
                w_ += w[a + j]
                v_ += v[a + j]
        items2.append([w_, v_])
    items2 = sorted(items2, key=lambda x: (x[0], -x[1]))

    a_items = []
    pre_v = 0
    for i in range(len(items1)):
        if items1[i][0] > W:
            break
        if items1[i][1] > pre_v:
            a_items.append(items1[i])
            pre_v = items1[i][1]
    a_items.insert(0, [0, 0])

    b_items = []
    pre_v = 0
    for i in range(len(items2)):
        if items2[i][0] > W:
            break
        if items2[i][1] > pre_v:
            b_items.append(items2[i])
            pre_v = items2[i][1]
    b_items.insert(0, [0, 0])
    b_items.append([10 ** 20, 0])
    b_w = [x[0] for x in b_items]

    ans = 0
    for i in range(len(a_items)):
        w_ = W - a_items[i][0]
        idx = bisect.bisect_left(b_w, w_) - 1
        if a_items[i][0] + b_items[idx][0] <= W:
            ans = max(ans, a_items[i][1] + b_items[idx][1])
        idx = bisect.bisect_left(b_w, w_)
        if a_items[i][0] + b_items[idx][0] <= W:
            ans = max(ans, a_items[i][1] + b_items[idx][1])
    print(ans)


# max_w <= 1000
def solve2():
    global n, W, items
    # wのdp
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(n):
        for j in range(w[i]):
            dp[i + 1][j] = dp[i][j]
        for j in range(w[i], W + 1):
            dp[i + 1][j] = max(dp[i][j], dp[i + 1][j - 1], dp[i][j - w[i]] + v[i])
    ans = 0
    for i in range(W + 1):
        ans = max(ans, dp[n][i])
    print(ans)


# max_v <= 1000
def solve3():
    global n, W, items
    # vのdp
    sum_v = 0
    for i in range(n):
        sum_v += v[i]
    dp = [[INF for _ in range(sum_v + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(n):
        for j in range(v[i]):
            dp[i + 1][j] = dp[i][j]
        for j in range(v[i], sum_v + 1):
            dp[i + 1][j] = min(dp[i][j], dp[i][j - v[i]] + w[i])
    ans = 0
    for i in range(len(dp[n])):
        if dp[n][i] <= W:
            ans = i
    print(ans)


if n <= 30:
    solve1()
elif max_w <= 1000:
    solve2()
else:
    solve3()
