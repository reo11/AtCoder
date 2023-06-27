from typing import List, Tuple
import time
import random
import math
from collections import defaultdict, deque

TIMELIMIT = 1.8
HEIGHT = 30
start_time = time.time()

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
        self.places = self.init_places.copy()
        self.score = 0
        self.pos = init_pos.copy()
        self.ball_size = HEIGHT * (HEIGHT + 1) // 2

    def place_str(self, x, y):
        return f"{x}_{y}"

    def up(self, x: int, y: int) -> List[Tuple[int, int]]:
        if x == 0:
            return []
        elif y == 0:
            return [(x - 1, y)]
        else:
            return [(x - 1, y - 1), (x - 1, y)]

    def down(self, x: int, y: int) -> List[Tuple[int, int]]:
        if y == HEIGHT - 1:
            return []
        else:
            return [(x + 1, y), (x + 1, y + 1)]

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

    def greedy(self):
        # 小さい方から一番上まで持っていく
        process = []
        for target_num in range(self.ball_size):
            current_x, current_y = self.places["place"][target_num]
            while True:
                up_list = self.up(current_x, current_y)
                if len(up_list) == 0:
                    # 一番上まで来た
                    break
                else:
                    # できるだけ上に持っていく
                    # 大きい方と交換
                    candicate = [-1, -1, -1]
                    for x, y in up_list:
                        num = self.places["number"][self.place_str(x, y)]
                        if num > target_num:
                            if num > candicate[0]:
                                candicate = [num, x, y]
                    if candicate[0] == -1:
                        break
                    process.append([current_x, current_y, candicate[1], candicate[2]])
                self.update_places(process[-1])
                current_x, current_y = self.places["place"][target_num]
        score = self.calc_score(process)
        return process, score


if __name__ == "__main__":
    init_pos = Model.get_input()
    model = Model(init_pos)
    process, score = model.greedy()
    model.output(process)
    # print(score)