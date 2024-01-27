from collections import deque, Counter
n, m = map(int, input().split())
x = list(map(int, input().split()))

# xと(x+1)mod nを繋いでいるので経路は時計回りか反時計回り
# 最初に適当に最短になるように移動させて、最も通行回数が少ない辺を削除する
# 通行回数が少ない辺が複数ある場合は全部試す？（未証明だが一旦1箇所で試す）

# 累積和の差分を格納
counter = [0] * (2 * (n + 1))
q = deque(x)

current_num = q.popleft()
cost = 0
while q:
    next_num = q.popleft()
    max_num = max(current_num, next_num)
    min_num = min(current_num, next_num)
    # 時計回り
    diff1 = max_num - min_num
    # 反時計回り
    diff2 = (n + min_num) - max_num
    if diff1 < diff2:
        counter[min_num] += diff2 - diff1
        counter[max_num] -= diff2 - diff1
    elif diff1 > diff2:
        counter[max_num] += diff1 - diff2
        counter[min_num + n] -= diff1 - diff2

    cost += min(diff1, diff2)
    # print(cost, current_num, next_num, diff1, diff2)
    current_num = next_num
# print(counter)
# 累積和
losses = [0] * (2 * (n + 1))
for i in range(1, 2 * (n + 1)):
    losses[i] += losses[i - 1] + counter[i]

for i in range(1, n + 1):
    losses[i] = losses[i] + losses[n + i]
print(cost + min(losses[1:n + 1]))
