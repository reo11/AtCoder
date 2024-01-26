import queue
from typing import List, Tuple


class BreadthFirstSearch:
    """幅優先探索"""

    def __init__(
        self,
        h: int,
        w: int,
        start_xy: Tuple[int, int],
        goal_xy: Tuple[int, int],
        board: List[List[str]],
    ) -> None:
        self.h, self.w = h, w
        (self.sx, self.sy) = start_xy
        (self.gx, self.gy) = goal_xy
        self.board = board
        self.hist = [[False] * w for i in range(h)]

    def get_step(self, wall: str = "#") -> int:
        """
        区切り文字を指定する(デフォルトは#)
        ゴールに着くまでの最短距離を出力
        ゴールにたどり着かない場合は0を出力
        """
        q: queue.Queue = queue.Queue()
        q.put((self.sx, self.sy))
        step = 0
        count = 1
        next_count = 1
        ans = 0
        # キューが空になるまで
        while not q.empty():
            x, y = q.get()
            count -= 1
            if count == 0:
                step += 1
                count = next_count
                next_count = 0
            # ゴールにたどり着くまでのステップ
            if x == self.gx and y == self.gy:
                ans = step
                break
            for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                # 範囲内か
                if not (0 <= x + i <= w - 1) or not (0 <= y + j <= h - 1):
                    continue
                # 壁では無いか
                if self.board[y + j][x + i] == wall:
                    continue
                # 既に通ったところか
                if self.hist[y + j][x + i]:
                    continue
                # 通った印をつける
                self.hist[y + j][x + i] = True
                q.put((x + i, y + j))
                next_count += 1
        return ans


# 図の形
h, w = map(int, input().split())
# スタート地点
s_xy = (0, 0)
# ゴール
g_xy = (w - 1, h - 1)
# ボードの読み込み
board = [[i for i in list(str(input()))] for i in range(h)]
# 既に通ったかどうか
bfs = BreadthFirstSearch(h, w, s_xy, g_xy, board)
ans = bfs.get_step()
count_black = 0
for y in range(h):
    for x in range(w):
        if board[y][x] == "#":
            count_black += 1
if ans == 0:
    print("-1")
else:
    print(h * w - ans - count_black)
