from collections import deque

n = int(input())
a = list(map(int, input().split()))
a.sort()

# めぐる式二分探索
left = 0
right = 10**9 + 1
plus = 0
minus = 0
while right - left > 1:
    mid = (left + right) // 2
    # O(N)で手数を求める
    flag = False
    plus = 0
    minus = 0
    for a_i in a:
        if a_i > mid:
            minus += a_i - mid
        elif a_i < mid:
            plus += mid - a_i
    if plus > minus:
        right = mid
    else:
        left = mid
# min = left, max = rightとなるように操作する
# left, rightは理想値なので
cost = [0, 0]
for a_i in a:
    if a_i < left:
        cost[0] += left - a_i
    else:
        cost[1] += a_i - right
print(max(cost))
