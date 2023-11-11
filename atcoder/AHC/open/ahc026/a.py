import time
import os
import itertools
from collections import defaultdict, deque
from typing import List

TIME_LIMIT = 1.90
MAX_PROCESS = 5_000
INF = 10 ** 12

is_debug_mode = os.getenv("DEBUG_MODE", False)

class Model:
    def __init__(self, n, m, init_postions):
        self.n = n
        self.m = m
        self.queue = []
        self.v_positions = defaultdict(lambda: -1)
        self.mountains = [deque([]) for _ in range(m)]
        # 左が下、右が上
        for i, vs in enumerate(init_postions, start=1):
            for v in vs:
                self.v_positions[v] = i
                self.mountains[i - 1].append(v)
                self.queue.append(v)
        self.queue = deque(sorted(self.queue))
        self.cost_spent = 0
        self.ans = []
        self.bottoms_set = set()

    def score(self):
        return max(1, 10_000 - self.cost_spent)

    def mv(self, v, to_i):
        # 数字vを山iの上に移動させる
        # コストを返す
        # vがある山の位置を特定
        mountain_i = self.v_positions[v]
        stuck = deque([])
        for _ in reversed(range(len(self.mountains[mountain_i - 1]))):
            stuck.appendleft(self.mountains[mountain_i - 1].pop())
            if stuck[0] == v:
                break
        k = len(stuck)
        for _ in range(len(stuck)):
            v = stuck.popleft()
            self.mountains[to_i - 1].append(v)
            self.v_positions[v] = to_i
        self.cost_spent += k + 1
        return k + 1

    def update():
        pass

    def output_ans(self):
        out = []
        for vi, i in self.ans:
            out.append(f"{vi} {i}")
        print("\n".join(out))

    def find_zero_mountain(self):
        for i, m in enumerate(self.mountains, start=1):
            count = 0
            for v in m:
                if v not in self.bottoms_set:
                    count += 1
            if count == 0:
                return i
        return -1

    def pickup_top(self):
        # 一番上にある数字が現在取り除く対象の場合取り除く
        count = 0
        flag = True
        while flag and self.queue:
            flag = False
            i = self.v_positions[self.queue[0]]
            if self.mountains[i - 1][-1] == self.queue[0]:
                v = self.queue.popleft()
                self.v_positions[v] = -1
                self.ans.append([v, 0])
                self.mountains[i - 1].pop()
                flag = True
                count += 1
        return count > 0

    def sort_top(self, diff = 1):
        # 終盤の効率化
        # 一番上にあるもの同士がdiff以下の場合乗せる
        count = 0
        flag = True
        while flag:
            flag = False
            tops = dict()
            for i in range(1, self.m + 1):
                if len(self.mountains[i - 1]) > 0:
                    tops[self.mountains[i - 1][-1]] = i
            for i in tops.keys():
                for j in range(1, diff + 1):
                    if i + j in tops.keys():
                        if len(self.mountains[tops[i] - 1]) > 1 and self.mountains[tops[i] - 1][-2] < i + j and self.mountains[tops[i] - 1][-2] > i:
                            continue
                        self.ans.append([i, tops[i + j]])
                        self.mv(i, tops[i + j])
                        flag = True
                        count += 1
                        break
        return count > 0


    def zero_fix(self, zero_fix_pattern = 1):
        # ゼロ山がある場合、一番下にない最も小さい数字を移動させる
        zero_mountain = self.find_zero_mountain()
        flag = True
        while flag and zero_mountain != -1:
            self.pickup_top()
            zero_mountain = self.find_zero_mountain()
            flag = False
            if zero_mountain != -1:
                bottoms = set() # 対象外
                # 一番下にある数字は除外
                for m in self.mountains:
                    if len(m) == 0:
                        continue
                    bottoms.add(m[0])
                # 既にこの処理で移動させた数字は除外
                for num in self.bottoms_set:
                    bottoms.add(num)
                for num in reversed(self.queue):
                    if num not in bottoms:
                        self.ans.append([num, zero_mountain])
                        self.mv(num, zero_mountain)
                        if zero_fix_pattern == 2:
                            self.bottoms_set.add(num)
                        flag = True
                        break
                    elif num in bottoms and num not in self.bottoms_set:
                        if zero_fix_pattern == 2:
                            self.bottoms_set.add(num)

    def to_mountain(self, mountain_num):
        to_mountain = [INF, -1]
        candidates = set(list(range(1, self.m + 1)))
        candidates.discard(mountain_num)
        for i in range(len(self.queue)):
            mountain_i = self.v_positions[self.queue[i]]
            candidates.discard(mountain_i)
            if len(candidates) == 1:
                to_mountain = [INF, candidates.pop()]
                break

        if to_mountain[1] == -1:
            for mountain_i in range(1, self.m + 1):
                if mountain_i == mountain_num:
                    continue
                if to_mountain[0] >= len(self.mountains[mountain_i - 1]):
                    to_mountain = [len(self.mountains[mountain_i - 1]), mountain_i]
        return to_mountain[1]


    def fix_mountains(self, target_num, mountain_num, max_diff = 1000):
        # queueに入ってる数字の登場が最も遅い山に移動させる
        pre_num = -INF
        for i in reversed(range(len(self.mountains[mountain_num - 1]))):
            if self.mountains[mountain_num - 1][i] == target_num:
                break
            if pre_num - self.mountains[mountain_num - 1][i] > max_diff:
                to = self.to_mountain(mountain_num)
                ans_v = pre_num
                ans_i = to
                self.ans.append([ans_v, ans_i])
                self.mv(ans_v, ans_i)
            pre_num = self.mountains[mountain_num - 1][i]

        to = self.to_mountain(mountain_num)
        for i, v in enumerate(self.mountains[mountain_num - 1]):
            if v == target_num:
                ans_v = self.mountains[mountain_num - 1][i + 1]
                ans_i = to
                self.ans.append([ans_v, ans_i])
                self.mv(ans_v, ans_i)
                self.mountains[mountain_num - 1].pop()
                self.ans.append([target_num, 0])
                break

    def solve_naive(self, top_sort_diff=0, zero_fix_pattern=0, max_diff=1000):
        while self.queue:
            flag = True
            while flag:
                flag = False
                flag |= self.pickup_top()
                if top_sort_diff >= 1:
                    flag |= self.sort_top(diff=top_sort_diff)
            if len(self.queue) == 0:
                break
            target_num = self.queue.popleft()
            mountain_num = self.v_positions[target_num]
            # 山の中にある場合
            self.fix_mountains(target_num, mountain_num, max_diff=max_diff)
            if zero_fix_pattern > 0:
                self.zero_fix(zero_fix_pattern) # ゼロ山に最も大きい数を移動させる

def main():
    start_at = time.time()
    n, m = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(m)]
    params = None
    model = Model(n, m, b)
    model.solve_naive()
    config = {
        "top_sort_diff": [0, 1, 2, 3],
        "zero_fix_pattern": [0, 1, 2],
        "max_diff": [5, 10, 15, 20, 25, 30, 35, 40, 50, 55, 60, 65, 70, 75, 80, 90, 100, 1000],
    }

    p = itertools.product(*config.values())

    for v in p:
        if time.time() - start_at > TIME_LIMIT:
            break
        model2 = Model(n, m, b)
        model2.solve_naive(*v)
        if len(model2.ans) > MAX_PROCESS:
            continue
        # print(v, model2.score())
        if model.score() < model2.score():
            model = model2
            params = v

    model.output_ans()
    if is_debug_mode:
        print(model.score())
        print(params)
main()