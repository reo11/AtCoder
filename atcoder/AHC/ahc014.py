import math
import random
import time
from collections import deque
from typing import Any, List

start_time = time.time()
EPS = 0.0000001
DIRECTIONS = [-1, 0, 1]
SIDE_SIMBOLS = {"|": 0, "-": 1, "/": 2, "\\": 3}


class Coordinate:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()


class Process:
    def __init__(
        self, c: Coordinate, sides: List[Any], coordinates: List[Coordinate]
    ) -> None:
        self.coordinate = c
        self.sides = sides
        self.coordinates = coordinates

    def __str__(self):
        return f"{self.coordinate}\n{self.sides}\n"

    def __repr__(self):
        return self.__str__()


class CoordinateController:
    def __init__(self, size: int, m: int) -> None:
        self.size = size
        self.m = m
        self.center = (self.size - 1) / 2
        # 座標に点が存在しているか
        self.coordinates = [[False for _ in range(size)] for _ in range(size)]
        # 座標一覧を高速に取得できるように
        self.coordinates_list = []
        # 辺が存在しているか
        self.sides = [
            [[False for _ in range(4)] for _ in range(size)] for _ in range(size)
        ]
        self.answers = []
        self.processes = []

    def sort_coordinates(self, coordinates: List[Coordinate]) -> List[Coordinate]:
        return sorted(coordinates, key=lambda x: (x.x, x.y))

    def add_coordinate(self, c: Coordinate) -> None:
        """
        座標に点を追加
        """
        self.coordinates[c.y][c.x] = True
        self.coordinates_list.append(
            [abs(self.center - c.x) + abs(self.center - c.y), c]
        )
        self.coordinates_list = sorted(self.coordinates_list, key=lambda c: c[0])

    def delete_coordinate(self, c: Coordinate) -> None:
        """
        座標を削除

        Args:
            c (Coordinate): 座標
        """
        self.coordinates[c.y][c.x] = False
        new_coordinates_list = []
        for dist, c_i in self.coordinates_list:
            if c.x == c_i.x and c.y == c_i.y:
                continue
            new_coordinates_list.append([dist, c_i])
        self.coordinates_list = new_coordinates_list

    def all_side_coordinates(self, c1: Coordinate, c2: Coordinate) -> None:
        sides = []
        # 2頂点間の点を列挙（追加はしない）
        # 小さい方から見ると、上、右上、右、右下のいずれかに絞れる
        assert self.is_valid_angle(c1, c2), f"{c1}, {c2}"

        sorted_c = self.sort_coordinates([c1, c2])
        x = sorted_c[0].x
        y = sorted_c[0].y
        if sorted_c[0].x == sorted_c[1].x:
            # 上
            while y <= sorted_c[1].y:
                sides.append(Coordinate(x=x, y=y))
                y += 1
        elif sorted_c[0].y == sorted_c[1].y:
            # 右
            while x <= sorted_c[1].x:
                sides.append(Coordinate(x=x, y=y))
                x += 1
        elif (sorted_c[1].x - sorted_c[0].x) == (sorted_c[1].y - sorted_c[0].y):
            # 右上
            while x <= sorted_c[1].x and y <= sorted_c[1].y:
                sides.append(Coordinate(x=x, y=y))
                x += 1
                y += 1
        else:
            # 右下
            while x <= sorted_c[1].x and y >= sorted_c[1].y:
                sides.append(Coordinate(x=x, y=y))
                x += 1
                y -= 1
        return sides

    def add_uni_side(self, c1: Coordinate, c2: Coordinate) -> List[int]:
        """
        最小の辺を追加
        """
        assert self.is_valid_angle(c1, c2), f"{c1}, {c2}"
        assert self.is_single_unit(c1, c2)

        sorted_c = self.sort_coordinates([c1, c2])
        if sorted_c[0].x == sorted_c[1].x:
            # 上
            symbol_num = SIDE_SIMBOLS["|"]
        elif sorted_c[0].y == sorted_c[1].y:
            # 右
            symbol_num = SIDE_SIMBOLS["-"]
        elif (sorted_c[1].x - sorted_c[0].x) == (sorted_c[1].y - sorted_c[0].y):
            # 右上
            symbol_num = SIDE_SIMBOLS["/"]
        else:
            # 右下
            symbol_num = SIDE_SIMBOLS["\\"]

        assert not self.sides[sorted_c[0].y][sorted_c[0].x][symbol_num]
        self.sides[sorted_c[0].y][sorted_c[0].x][symbol_num] = True

        return [sorted_c[0].x, sorted_c[0].y, symbol_num]

    def add_side(self, c1: Coordinate, c2: Coordinate) -> List[List[int]]:
        """
        2頂点間に辺を追加
        """
        coordinates = self.all_side_coordinates(c1, c2)
        uni_sides_list = []

        for i in range(len(coordinates) - 1):
            uni_sides_list.append(self.add_uni_side(coordinates[i], coordinates[i + 1]))
        return uni_sides_list

    def delete_sides(self, sides: List[List[int]]):
        for side in sides:
            x = side[0]
            y = side[1]
            symbol_num = side[2]
            self.sides[y][x][symbol_num] = False

    def is_valid_angle(self, c1: Coordinate, c2: Coordinate) -> bool:
        """
        角度が平行か45度
        """
        # 平行
        #  - x, yの片方の変化が0
        # 45度
        #  - x, yの変化の絶対値が一致
        def is_parallel(c1: Coordinate, c2: Coordinate):
            return (c1.x - c2.x) == 0 or (c1.y - c2.y) == 0

        def is_forty_five(c1: Coordinate, c2: Coordinate):
            return abs(c1.x - c2.x) == abs(c1.y - c2.y)

        def not_same_coordinate(c1: Coordinate, c2: Coordinate):
            return not (c1.x == c2.x and c1.y == c2.y)

        return (is_parallel(c1, c2) or is_forty_five(c1, c2)) and not_same_coordinate(
            c1, c2
        )

    def is_single_unit(self, c1: Coordinate, c2: Coordinate) -> bool:
        """
        最小のペアか
        - 距離が1
        - 距離がルート2
        """
        distance = math.sqrt((c1.x - c2.x) ** 2 + (c1.y - c2.y) ** 2)
        return 1.00 - EPS <= distance and distance <= math.sqrt(2) + EPS

    def uni_side_already_exist(self, c1: Coordinate, c2: Coordinate) -> bool:
        assert self.is_valid_angle(c1, c2), f"{c1}, {c2}"
        assert self.is_single_unit(c1, c2)

        sorted_c = self.sort_coordinates([c1, c2])
        if sorted_c[0].x == sorted_c[1].x:
            # 上
            return self.sides[sorted_c[0].y][sorted_c[0].x][SIDE_SIMBOLS["|"]]
        elif sorted_c[0].y == sorted_c[1].y:
            # 右
            return self.sides[sorted_c[0].y][sorted_c[0].x][SIDE_SIMBOLS["-"]]
        elif (sorted_c[1].x - sorted_c[0].x) == (sorted_c[1].y - sorted_c[0].y):
            # 右上
            return self.sides[sorted_c[0].y][sorted_c[0].x][SIDE_SIMBOLS["/"]]
        else:
            # 右下
            return self.sides[sorted_c[0].y][sorted_c[0].x][SIDE_SIMBOLS["\\"]]

    def is_valid_sides(self, coordinates: List[Coordinate]) -> bool:
        is_valid = True
        for i in range(4):
            if i < 3:
                all_coordinates = self.all_side_coordinates(
                    coordinates[i], coordinates[i + 1]
                )
            else:
                all_coordinates = self.all_side_coordinates(
                    coordinates[3], coordinates[0]
                )
            for i in range(len(all_coordinates) - 1):
                is_valid &= not self.uni_side_already_exist(
                    all_coordinates[i], all_coordinates[i + 1]
                )
            if not is_valid:
                break
        return is_valid

    def is_valid_coordinates(self, coordinates: List[Coordinate]) -> bool:
        is_valid = True
        for i in range(4):
            if i < 3:
                all_coordinates = self.all_side_coordinates(
                    coordinates[i], coordinates[i + 1]
                )
            else:
                all_coordinates = self.all_side_coordinates(
                    coordinates[3], coordinates[0]
                )
            for c in all_coordinates[1:-1]:
                is_valid &= not self.coordinates[c.y][c.x]
            if not is_valid:
                break
        return is_valid

    def is_valid_square(self, coordinates: List[Coordinate]) -> bool:
        assert len(coordinates) == 4
        is_valid = True
        is_valid &= self.is_valid_coordinates(coordinates)
        is_valid &= self.is_valid_sides(coordinates)
        return is_valid

    def add_square_sides(self, coordinates: List[Coordinate]) -> List[List[Any]]:
        assert len(coordinates) == 4
        uni_sides_list = []
        for i in range(3):
            uni_sides_list.extend(self.add_side(coordinates[i], coordinates[i + 1]))
        uni_sides_list.extend(self.add_side(coordinates[-1], coordinates[0]))
        return uni_sides_list

    def add_square(
        self, new_coordinate: Coordinate, four_coordinates: List[Coordinate]
    ) -> List[List[int]]:
        self.add_coordinate(new_coordinate)
        sides = self.add_square_sides(four_coordinates)
        return sides

    def calc_score(self) -> float:
        def sum_q():
            q_score = 0
            s = 0
            w = [
                [
                    (x - self.center) ** 2 + (y - self.center) ** 2 + 1
                    for x in range(self.size)
                ]
                for y in range(self.size)
            ]
            for i in range(self.size):
                for j in range(self.size):
                    s += w[i][j]
                    if self.coordinates[i][j]:
                        q_score += w[i][j]
            return q_score / s

        return round(10 ** 6 * (self.size ** 2 / self.m) * sum_q())

    def add_process(self, sides: List[Any], coordinates: List[Coordinate]) -> None:
        p = Process(c=coordinates[0], sides=sides, coordinates=coordinates)
        self.processes.append(p)

    def display_answers(self) -> None:
        if len(self.processes) == 0:
            print(0)
        else:
            out = f"{len(self.processes)}\n"
            for i, p in enumerate(self.processes):
                l = []
                for c in p.coordinates:
                    l.append(c.x)
                    l.append(c.y)
                out += " ".join(map(str, l))
                if i < len(self.processes) - 1:
                    out += "\n"
            print(out)

    def undo(self) -> None:
        if len(self.processes) <= 0:
            return
        last_process = self.processes.pop(-1)
        new_coordinate = last_process.coordinate
        new_sides = last_process.sides
        self.delete_coordinate(new_coordinate)
        self.delete_sides(new_sides)


# 探索


def is_valid_area(x: int, size: int) -> bool:
    return 0 <= x and x < size


def solve_one() -> CoordinateController:
    """
    step1: 1つの点に注目した時、8方向に対して候補の点が存在するか調べる: 8*O(n)=O(n)
    step2: 2つの点が確定した時に調べる該当方向を調べる: O(n)
    step3: 3つの点が確定した時、4つ目の点が存在しなければ確定して追加
    """
    # input
    n, m = map(int, input().split())
    try_num = 1
    process_queue = deque()
    coordinate_controllers = [CoordinateController(size=n, m=m) for _ in range(try_num)]
    for i in range(m):
        x_i, y_i = map(int, input().split())
        c = Coordinate(x=x_i, y=y_i)
        for i in range(try_num):
            coordinate_controllers[i].add_coordinate(c)
            process_queue.append(i)
    # print(f"Before: {coordinate_controller.calc_score()}")

    count = 0
    while time.time() - start_time < 4.7:
        # step1
        c_num = process_queue.popleft()
        coordinate_controller = coordinate_controllers[c_num]
        if random.random() <= 0.001:
            coordinate_controller.undo()
            continue
        before_score = coordinate_controller.calc_score()
        choice_w = []
        for dist, coord in coordinate_controller.coordinates_list:
            if dist == 0:
                dist = 0.5
            choice_w.append(1)
        _, first_coordinate = random.choices(
            coordinate_controller.coordinates_list, weights=choice_w
        )[0]
        dx = 0
        dy = 0
        while dx == 0 and dy == 0:
            dx = random.choice(DIRECTIONS)
            dy = random.choice(DIRECTIONS)

        second_x = first_coordinate.x + dx
        second_y = first_coordinate.y + dy
        rand = random.random()
        while is_valid_area(second_x, n) and is_valid_area(second_y, n):
            if coordinate_controller.coordinates[second_y][second_x]:
                # 見つかった
                rand = 1.0
                break
            if rand < 0.98:
                break
            second_x += dx
            second_y += dy
        if rand < 0.98:
            process_queue.append(c_num)
            continue
        if not ((0 <= second_x and second_x < n) and (0 <= second_y and second_y < n)):
            process_queue.append(c_num)
            continue
        if not coordinate_controller.coordinates[second_y][second_x]:
            process_queue.append(c_num)
            continue

        second_coordinate = Coordinate(x=second_x, y=second_y)
        second_dxys = [[dy, -dx], [-dy, dx]]
        for dxy in second_dxys:
            dx = dxy[0]
            dy = dxy[1]
            for i in range(1, n):
                if (
                    is_valid_area(first_coordinate.x + i * dx, n)
                    and is_valid_area(second_coordinate.x + i * dx, n)
                    and is_valid_area(first_coordinate.y + i * dy, n)
                    and is_valid_area(second_coordinate.y + i * dy, n)
                ):
                    if (
                        coordinate_controller.coordinates[first_coordinate.y + i * dy][
                            first_coordinate.x + i * dx
                        ]
                        ^ coordinate_controller.coordinates[
                            second_coordinate.y + i * dy
                        ][second_coordinate.x + i * dx]
                    ):
                        if coordinate_controller.coordinates[
                            first_coordinate.y + i * dy
                        ][first_coordinate.x + i * dx]:
                            forth_coordinate = Coordinate(
                                x=first_coordinate.x + i * dx,
                                y=first_coordinate.y + i * dy,
                            )
                            third_coordinate = Coordinate(
                                x=second_coordinate.x + i * dx,
                                y=second_coordinate.y + i * dy,
                            )
                            add_c = third_coordinate
                            answer_coordinates = [
                                third_coordinate,
                                forth_coordinate,
                                first_coordinate,
                                second_coordinate,
                            ]
                        else:
                            third_coordinate = Coordinate(
                                x=second_coordinate.x + i * dx,
                                y=second_coordinate.y + i * dy,
                            )
                            forth_coordinate = Coordinate(
                                x=first_coordinate.x + i * dx,
                                y=first_coordinate.y + i * dy,
                            )
                            add_c = forth_coordinate
                            answer_coordinates = [
                                forth_coordinate,
                                first_coordinate,
                                second_coordinate,
                                third_coordinate,
                            ]

                        if coordinate_controller.is_valid_square(answer_coordinates):
                            sides = coordinate_controller.add_square(
                                add_c, answer_coordinates
                            )
                            coordinate_controller.add_process(
                                sides=sides, coordinates=answer_coordinates
                            )
                            break
                else:
                    break
        if before_score < coordinate_controller.calc_score():
            process_queue.appendleft(c_num)
            coordinate_controllers[c_num] = coordinate_controller
        else:
            process_queue.append(c_num)

    # 最もスコアが良いもの
    coordinate_controller = coordinate_controllers[0]
    print(coordinate_controller.calc_score())
    for i in range(1, try_num):
        print(coordinate_controllers[i].calc_score())
        if coordinate_controller.calc_score() < coordinate_controllers[i].calc_score():
            coordinate_controller = coordinate_controllers[i]
    return coordinate_controller


coordinate_controller = solve_one()
coordinate_controller.display_answers()

# print(f"After: {coordinate_controller.calc_score()}")
