from typing import List
import time
import random
import math
from collections import defaultdict, deque

TIMELIMIT = 1.8
HEIGHT = 30
start_time = time.time()


def sigmoid(x):
    return 1 / (1 + math.exp(-x))

class Model:
    def __init__(self, init_pos) -> None:
        self.init_pos = init_pos
        self.init_places = {
            "place": defaultdict(lambda: [-1, -1]),  # 番号→座標
            "number": defaultdict(lambda: -1) # 座標→番号
        }
        for i in range(HEIGHT):
            for j in range(i + 1):
                self.init_places["place"][self.init_pos[i][j]] = [i, j]
                self.init_places["number"][self.place_str(i, j)] = self.init_pos[i][j]
        # print(self.init_places)
        self.places = self.init_places.copy()
        self.score = 0
        self.pos = init_pos.copy()
        self.ball_size = HEIGHT * (HEIGHT + 1) // 2

    def place_str(self, x, y):
        return f"{x}_{y}"

    def invalid_e_count(self, pos) -> None:
        count_invalid = []
        for i in range(HEIGHT - 1):
            for j in range(i + 1):
                if pos[i][j] > pos[i + 1][j]:
                    count_invalid.append([[i, j], [i + 1, j]])
                if pos[i][j] > pos[i + 1][j + 1]:
                    count_invalid.append([[i, j], [i + 1, j]])
        return count_invalid

    def get_input() -> None:
        init_pos = []
        for _ in range(HEIGHT):
            pos_i = list(map(int, input().split()))
            init_pos.append(pos_i)
        return init_pos

    def output(self, process: List[List[int]]) -> None:
        # 入れ替え手順を出力
        ans = []
        ans.append(len(process))
        assert len(process) <= 10_000
        for x0, y0, xd0, yd0 in process:
            ans.append(f"{x0} {y0} {xd0} {yd0}")
        print(*ans, sep="\n")

    def calc_score(self, process: List[List[int]]) -> int:
        k = len(process)
        pos = [[] for _ in range(HEIGHT)]
        for i in range(HEIGHT):
            for j in range(i + 1):
                pos[i].append(self.places["number"][self.place_str(i, j)])
        invalid_e = self.invalid_e_count(pos)
        if len(invalid_e) == 0:
            return 100_000 - 5 * k
        else:
            return 50_000 - 50 * len(invalid_e)

    def update_places(self, pos_i: List[int]) -> None:
        x0, y0, xd0, yd0 = pos_i
        first_num = self.places["number"][self.place_str(x0, y0)]
        second_num = self.places["number"][self.place_str(xd0, yd0)]
        self.places["place"][first_num] = [xd0, yd0]
        self.places["place"][second_num] = [x0, y0]
        self.places["number"][self.place_str(x0, y0)] = second_num
        self.places["number"][self.place_str(xd0, yd0)] = first_num

    def calc_process(self, pos) -> List[List[int]]:
        # 大きい方を選びながら上から埋める
        # 同じ高さになったら横移動
        process = []
        for i in range(HEIGHT):
            for j in range(i + 1):
                target_num = pos[i][j]
                current_x, current_y = self.places["place"][target_num]
                # print("debug", i, j, target_num, current_x, current_y)
                # print(i, j, target_num, current_x, current_y)
                # time.sleep(0.4)
                if current_x == i and current_y == j:
                    continue
                while current_x != i or current_y != j:
                    # print(i, j, current_x, current_y)
                    # time.sleep(0.5)
                    if current_y != j:
                        # 横に移動
                        # print("横移動")
                        if current_y > j:
                            process.append([current_x, current_y, current_x, current_y - 1])
                        elif current_y < j:
                            process.append([current_x, current_y, current_x, current_y + 1])
                        else:
                            break
                    elif current_x > i:
                        # print("上移動")
                        # 上に移動
                        upper_x = current_x - 1
                        upper_ys = list(filter(lambda x: x >= 0 and x <= upper_x, [current_y - 1, current_y]))
                        # print("upper_ys", upper_ys)
                        if len(upper_ys) == 0:
                            break
                        elif len(upper_ys) == 1:
                            process.append([current_x, current_y, current_x - 1, upper_ys[0]])
                        else:
                            # 大きい方を下に下げる
                            upper_y1_num = self.places["number"][self.place_str(upper_x, upper_ys[0])]
                            upper_y2_num = self.places["number"][self.place_str(upper_x, upper_ys[1])]
                            if upper_y1_num > upper_y2_num:
                                process.append([current_x, current_y, current_x - 1, upper_ys[0]])
                            else:
                                process.append([current_x, current_y, current_x - 1, upper_ys[1]])
                    elif current_x < i:
                        # 下移動
                        lower_x = current_x + 1
                        lower_ys = list(filter(lambda x: x >= 0 and x <= lower_x, [current_y + 1, current_y]))
                        # print("lower_ys", lower_ys)
                        if len(lower_ys) == 0:
                            break
                        elif len(lower_ys) == 1:
                            process.append([current_x, current_y, current_x - 1, lower_ys[0]])
                        else:
                            # 小さい方を上に上げる
                            lower_y1_num = self.places["number"][self.place_str(lower_x, lower_ys[0])]
                            lower_y2_num = self.places["number"][self.place_str(lower_x, lower_ys[1])]
                            if lower_y1_num < lower_y2_num:
                                process.append([current_x, current_y, current_x + 1, lower_ys[0]])
                            else:
                                process.append([current_x, current_y, current_x + 1, lower_ys[1]])
                    # valid check
                    assert self.is_valid(process[-1])
                    self.update_places(process[-1])
                    current_x, current_y = self.places["place"][target_num]
        return process

    def is_valid(self, process: List[int]) -> bool:
        # 逆操作をしてみてvalidかどうかを判定
        x0, y0, xd0, yd0 = process
        if y0 > x0 or yd0 > xd0:
            return False
        if (x0 == xd0 - 1 and y0 == yd0 - 1) or \
            (x0 == xd0 - 1 and y0 == yd0) or \
            (x0 == xd0 and y0 == yd0 - 1) or \
            (x0 == xd0 and y0 == yd0 + 1) or \
            (x0 == xd0 + 1 and y0 == yd0) or \
            (x0 == xd0 + 1 and y0 == yd0 + 1):
            return True
        else:
            return False

    def solve1(self):
        # [0], [1, 2], [3, 4, 5]の順にする
        pos = []
        num = 0
        for i in range(HEIGHT):
            pos_i = [num + j for j in range(i + 1)]
            pos.append(pos_i)
            num += i + 1
        process = self.calc_process(pos)
        self.best_pos = pos
        return pos, process

    def solve2(self):
        # 後ろから順に下と比べて大きかったら下へを繰り返す
        process = []
        for target_num in reversed(range(self.ball_size)):
            # print(target_num)
            current_x, current_y = self.places["place"][target_num]
            while True:
                if current_x == HEIGHT - 1:
                    break
                lower_1 = [self.places["number"][self.place_str(current_x + 1, current_y)], current_x + 1, current_y]
                lower_2 = [self.places["number"][self.place_str(current_x + 1, current_y + 1)], current_x + 1, current_y + 1]
                if lower_1[0] > target_num and lower_2[0] > target_num:
                    break
                elif lower_1[0] < target_num and lower_2[0] < target_num:
                    if lower_1[0] > lower_2[0]:
                        # lower_2と入れ替える
                        process.append([current_x, current_y, lower_2[1], lower_2[2]])
                    else:
                        process.append([current_x, current_y, lower_1[1], lower_1[2]])
                elif lower_1[0] < target_num:
                    process.append([current_x, current_y, lower_1[1], lower_1[2]])
                else:
                    process.append([current_x, current_y, lower_2[1], lower_2[2]])
                self.update_places(process[-1])
                current_x, current_y = self.places["place"][target_num]
        return process

    def solve3(self, prob=1.0):
        # solve2に確率で小さいのを上にする処理を加える
        process = []
        target_nums = deque([])
        for target_num in reversed(range(self.ball_size)):
            target_nums.append(target_num)
        completed = defaultdict(lambda: False)
        while len(target_nums) > 0:
            not_random = True
            if random.random() > prob and len(target_nums) > 1:
                not_random = False
                target_num = random.choice(target_nums)
                if completed[target_num]:
                    target_nums.popleft()
                    if len(target_nums) == 0:
                        break
                    target_num = target_nums[0]
                    not_random = True
            else:
                target_num = target_nums[0]
                if completed[target_num]:
                    target_nums.popleft()
                    if len(target_nums) == 0:
                        break
                    target_num = target_nums[0]

            current_x, current_y = self.places["place"][target_num]
            def go_down(target_num, current_x, current_y):
                if current_x == HEIGHT - 1:
                    completed[target_num] = True
                    return None
                lower_1 = [self.places["number"][self.place_str(current_x + 1, current_y)], current_x + 1, current_y]
                lower_2 = [self.places["number"][self.place_str(current_x + 1, current_y + 1)], current_x + 1, current_y + 1]
                if lower_1[0] > target_num and lower_2[0] > target_num:
                    completed[target_num] = True
                    return None
                elif lower_1[0] < target_num and lower_2[0] < target_num:
                    if lower_1[0] > lower_2[0]:
                        # lower_2と入れ替える
                        return [current_x, current_y, lower_2[1], lower_2[2]]
                    else:
                        return [current_x, current_y, lower_1[1], lower_1[2]]
                elif lower_1[0] < target_num:
                    return [current_x, current_y, lower_1[1], lower_1[2]]
                else:
                    return [current_x, current_y, lower_2[1], lower_2[2]]
            def go_up(target_num, current_x, current_y):
                if current_x == 0:
                    return None
                upper_1 = [self.places["number"][self.place_str(current_x - 1, current_y)], current_x - 1, current_y]
                if current_y > 0:
                    upper_2 = [self.places["number"][self.place_str(current_x - 1, current_y - 1)], current_x - 1, current_y - 1]
                    if upper_1[0] > target_num and upper_2[0] > target_num:
                        if upper_1[0] > upper_2[0]:
                            return [current_x, current_y, upper_1[1], upper_1[2]]
                        else:
                            return [current_x, current_y, upper_2[1], upper_2[2]]
                    elif upper_1[0] > target_num:
                        return [current_x, current_y, upper_1[1], upper_1[2]]
                    elif upper_2[0] > target_num:
                        return [current_x, current_y, upper_2[1], upper_2[2]]
                    else:
                        return None
                else:
                    if upper_1[0] > target_num:
                        return [current_x, current_y, upper_1[1], upper_1[2]]
                    else:
                        return None
            if not_random:
                process_i = go_down(target_num, current_x, current_y)
            else:
                process_i = go_up(target_num, current_x, current_y)
            if process_i is not None:
                process.append(process_i)
                self.update_places(process[-1])
        score = self.calc_score(process)
        return process, score


if __name__ == "__main__":
    init_pos = Model.get_input()
    best_set = [-1, [], None]
    while time.time() - start_time < 1.8:
        prob = random.choice([0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
        model = Model(init_pos)
        # pos, process = model.solve1()
        process, score = model.solve3(prob)
        if score > best_set[0]:
            best_set = [score, process, model]
    score, process, model = best_set
    model.output(process)