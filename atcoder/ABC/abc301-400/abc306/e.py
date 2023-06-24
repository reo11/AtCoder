import sys
import heapq
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()


n, k, q = map(int, input().split())
xy = []
for _ in [0]*q:
    x, y = map(int, input().split())
    xy.append((x, y))

# 1. K要素の優先度付きキューと2. N-K要素の優先度付きキューを用意する
# 1は小さい方を高速に取得
# 2は大きい方を高速に取得
a = [0 for _ in range(n)]
fa = 0
ans = []
first_queue = [[0, -1, -1] for _ in range(k)]
second_queue = [[0, -1, -1] for _ in range(n - k)]
first_set = set()
second_set = set()
# 各ユーザの最新の行動を記録
user_memo = defaultdict(lambda: -1)
heapq.heapify(first_queue)
heapq.heapify(second_queue)

for i in range(q):
    x, y = xy[i]
    tmp_value = a[x - 1]
    a[x - 1] = y
    # 1の要素の最小値以上かどうかを確認
    min_value, idx, action_i = heapq.heappop(first_queue)
    if user_memo[idx] != action_i or idx not in first_set:
        while user_memo[idx] == action_i and idx in first_set:
            # validな値を取り出す
            min_value, idx, action_i = heapq.heappop(first_queue)

    if min_value < y:
        # 1のキューに入れる
        # 今どちらにいるか
        if x - 1 in first_set:
            fa = fa + y - tmp_value
        else:
            # secondにいる場合
            fa = fa + y - min_value
            second_set.discard(x - 1)
            first_set.add(x - 1) # secondのに元々いたやつは移動
            first_set.discard(idx)
            second_set.add(idx)  # firstのminは移動
        heapq.heappush(first_queue, [y, x - 1, i])
        heapq.heappush(second_queue, [-min_value, idx, action_i])
    else:
        # 戻す
        heapq.heappush(first_queue, [min_value, idx, action_i])
        if x - 1 in first_set:
            if x - 1 == idx:
                # 自分自身を更新するだけ
                fa = fa + y - tmp_value
                heapq.heappush(first_queue, [y, x - 1, i])
            else:
                max_value, s_idx, s_action_i = heapq.heappop(second_queue)
                max_value = -max_value
                if user_memo[s_idx] != s_action_i or s_idx not in second_set:
                    while user_memo[s_idx] == s_action_i and s_idx in second_set:
                        # validな値を取り出す
                        max_value, s_idx, s_action_i = heapq.heappop(second_queue)
                        max_value = -max_value
                fa = fa - tmp_value + max_value
                heapq.heappush(first_queue, [max_value, s_idx, s_action_i])
                heapq.heappush(second_queue, [-min_value, idx, action_i])
                first_set.discard(x - 1)
                second_set.add(x - 1)  # firstのに元々いたやつは移動
                second_set.discard(s_idx)
                first_set.add(s_idx)   # secondのmaxは移動
                heapq.heappush(second_queue, [-y, x - 1, i])
        else:
            heapq.heappush(second_queue, [-y, x - 1, i])
    print("first_queue", fa, first_queue)
    print("second_queue", fa, second_queue)
    ans.append(fa)
    user_memo[x - 1] = i
print(*ans, sep='\n')

