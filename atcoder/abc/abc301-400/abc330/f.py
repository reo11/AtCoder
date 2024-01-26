from collections import defaultdict, deque

INF = float("inf")
n, k = map(int, input().split())
xy = []

for _ in range(n):
    x, y = map(int, input().split())
    xy.append((x, y))
    if n == 1:
        xy.append(x, y)

# 作成可能な正方形の辺の長さを2分探索する
l = -1
r = 10**10 + 1

# queueに入ったデータの両端の差をvalueにする
def calc_cost(value, queue):
    counter = [1, 1]
    left = queue.popleft()
    right = queue.pop()
    cost = 0
    while right - left > value:
        if len(queue) == 0:
            next_left = right - value
            next_right = left + value
        else:
            next_left = queue[0]
            next_right = queue[-1]
            if right - next_left < value:
                next_left = right - value
            if next_right - left < value:
                next_right = left + value
        cost1 = counter[0] * (next_left - left)
        cost2 = counter[1] * (right - next_right)
        if cost1 < cost2:
            if len(queue) > 0:
                queue.popleft()
            left = next_left
            counter[0] += 1
            cost += cost1
        else:
            if len(queue) > 0:
                queue.pop()
            right = next_right
            counter[1] += 1
            cost += cost2
    return cost, left, right


def judge(value, max_cost):
    x_queue = []
    y_queue = []
    for x, y in xy:
        x_queue.append(x)
        y_queue.append(y)
    x_queue = deque(list(sorted(x_queue)))
    y_queue = deque(list(sorted(y_queue)))
    cost_x, left_x, right_x = calc_cost(value, x_queue)
    cost_y, left_y, right_y = calc_cost(value, y_queue)
    print(
        value,
        cost_x + cost_y,
        (k - (cost_x + cost_y)),
        right_x - left_x,
        right_y - left_y,
    )
    return cost_x + cost_y <= max_cost


while r - l > 1:
    mid = (r + l) // 2
    if judge(mid, k):
        r = mid
    else:
        l = mid
print(l, r)
