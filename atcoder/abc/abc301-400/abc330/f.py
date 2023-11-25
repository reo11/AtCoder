from collections import defaultdict, deque
INF = float("inf")
n, k = map(int, input().split())
xy = []

pos_counter = defaultdict(lambda: defaultdict(lambda: 0))
min_max_x = [INF, -INF]
min_max_y = [INF, -INF]
for _ in range(n):
    x, y = map(int, input().split())
    xy.append((x, y))
    min_max_x[0] = min(min_max_x[0], x)
    min_max_x[1] = max(min_max_x[1], x)
    min_max_y[0] = min(min_max_y[0], y)
    min_max_y[1] = max(min_max_y[1], y)
    pos_counter["x"][x] += 1
    pos_counter["y"][y] += 1

# 作成可能な正方形の辺の長さを2分探索する
l = 0
r = 10 ** 9 + 1

def judge(value, max_cost):
    counter = defaultdict(lambda: 0)
    x_que = set()
    y_que = set()
    for x, y in xy:
        x_que.add(x)
        y_que.add(y)
        counter["x"][x] += 1
        counter["y"][y] += 1
    x_que = deque(list(sorted(x_que)))
    y_que = deque(list(sorted(y_que)))
    left = min_max_x[0]
    right = min_max_x[1]
    counter["left"] = pos_counter["x"][left]
    counter["right"] = pos_counter["x"][right]
    cost = 0
    while right - left > value:
        while len(x_que) > 0:
            if x_que[0] <= left:
                x_que.popleft()
            else:
                break
        while len(x_que) > 0:
            if x_que[-1] >= right:
                x_que.pop()
            else:
                break
        next_left, next_right = x_que[0], x_que[-1]
        # valueより小さくなってしまう場合調整
        if right - next_left < value:
            next_left = right - value
        if next_right - left < value:
            next_right = left + value
        cost_left = next_left - left
        cost_right = right - next_right
        if
        cost +=



while r - l > 1:
    mid = (r + l) // 2
    if judge(mid, k):
        l = mid
    else:
        r = mid
print(l)

