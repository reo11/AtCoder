import time
import os
import random
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
        self.done_set = set()

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
        self.ans.append([v, to_i])
        return k + 1

    def output_ans(self):
        out = []
        for vi, i in self.ans:
            out.append(f"{vi} {i}")
        print("\n".join(out))

    def pickup_top(self):
        # 一番上にある数字が現在取り除く対象の場合取り除く
        count = 0
        flag = True
        while flag and self.queue:
            flag = False
            i = self.v_positions[self.queue[0]]
            if len(self.mountains[i - 1]) == 0:
                continue
            if self.mountains[i - 1][-1] == self.queue[0]:
                v = self.queue.popleft()
                self.v_positions[v] = -1
                self.ans.append([v, 0])
                self.mountains[i - 1].pop()
                flag = True
                count += 1
        return count > 0

    def give_mountain(self, mountain_num):
        while len(self.mountains[mountain_num - 1]) > 0:
            self.pickup_top()
            if len(self.mountains[mountain_num - 1]) == 0:
                break
            from_v = self.mountains[mountain_num - 1][-1]
            to_i = [-1, -1]
            for i in range(1, self.m + 1):
                if i == mountain_num:
                    continue
                if len(self.mountains[i - 1]) == 0:
                    continue
                to_v = self.mountains[i - 1][-1]
                if to_v < from_v and to_i[0] < to_v:
                    to_i = [to_v, i]
            if to_i == [-1, -1]:
                # 乱択
                candidate_set = set()
                for ii in range(1, self.m + 1):
                    if ii == mountain_num:
                        continue
                    if ii in self.done_set:
                        continue
                    candidate_set.add(ii)
                if len(candidate_set) == 0:
                    # 候補がない場合は終了
                    return
                rand_i = random.choice(list(candidate_set))
                to_i = [-1, rand_i]
            self.mv(from_v, to_i[1])


    def get_mountain(self, mountain_num):
        current_num = INF
        for _ in range(1000):
            self.pickup_top()
            process = [-1, -1] # [v, from_i]
            for i in range(1, self.m + 1):
                if i == mountain_num:
                    continue
                if len(self.mountains[i - 1]) == 0:
                    continue
                if current_num < self.mountains[i - 1][-1]:
                    continue
                from_v = self.mountains[i - 1][-1]
                if process[0] < from_v:
                    process = [from_v, i]
            if process == [-1, -1]:
                break
            self.mv(process[0], mountain_num)
            current_num = process[0]
            # print(current_num, process)

    def fix_mountains(self):
        # queueに入ってる数字の登場が最も遅い山に移動させる
        from_num = self.v_positions[1]
        # from_numの一番上をto_numに移動させる
        self.done_set = set()
        while True:
            self.give_mountain(from_num)
            self.get_mountain(from_num)
            self.pickup_top()
            self.done_set.add(from_num)
            from_nums = [INF, -1]
            for next_num in range(1, self.m + 1):
                if next_num in self.done_set:
                    continue
                if self.queue and next_num == self.v_positions[self.queue[0]]:
                    from_nums = [INF, next_num]
                    break
                if from_nums[0] > len(self.mountains[next_num - 1]):
                    from_nums = [len(self.mountains[next_num - 1]), next_num]
            from_num = from_nums[1]
            if len(self.done_set) == self.m:
                break

    def solve_last(self):
        # 取りたいものの上を移動させる
        while self.queue:
            if self.v_positions[self.queue[0]] == -1:
                self.queue.popleft()
                continue
            mountain_num = self.v_positions[self.queue[0]]
            to_mountain = [INF, -1]
            for i in range(1, self.m + 1):
                if i == mountain_num:
                    continue
                if to_mountain[0] > len(self.mountains[i - 1]):
                    to_mountain = [len(self.mountains[i - 1]), i]
            self.mv(self.queue[0], to_mountain[1])
            self.pickup_top()

    def solve_naive(self):
        self.fix_mountains()
        self.solve_last()

def main():
    start_at = time.time()
    n, m = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(m)]
    params = None
    model = Model(n, m, b)
    model.solve_naive()

    model.output_ans()
    if is_debug_mode:
        print(model.score())
        print(params)
main()