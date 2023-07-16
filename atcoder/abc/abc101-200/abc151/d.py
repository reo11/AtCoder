import queue


class BreadthFirstSearch:
    def __init__(self, h, w, start_xy, board):
        self.h, self.w = h, w
        (self.sx, self.sy) = start_xy
        self.board = board
        self.hist = [[False] * w for i in range(h)]

    def get_step(self, wall="#"):
        """
        区切り文字を指定する(デフォルトは#)
        ゴールに着くまでの最短距離を出力
        ゴールにたどり着かない場合は0を出力
        """
        q = queue.Queue()
        q.put((self.sx, self.sy))
        self.hist[self.sy][self.sx] = True
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
        return step


# 図の形
h, w = map(int, input().split())
# ボードの読み込み
board = [[i for i in list(str(input()))] for i in range(h)]
# スタート地点
ans_ = []
for s_i in range(h):
    for s_j in range(w):
        if board[s_i][s_j] == "#":
            continue
        s_xy = (s_j, s_i)
        bfs = BreadthFirstSearch(h, w, s_xy, board[:])
        ans = bfs.get_step()
        ans_.append(ans)
print(max(ans_) - 1)
