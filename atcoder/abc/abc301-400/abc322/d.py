# 全探索するしかなさそう
import numpy as np
from functools import lru_cache

ps = []
for i in range(3):
    p = []
    for j in range(4):
        p.append(list(input()))
    p = np.array(p)
    # 横方向で.のみの行を削除
    idxs = []
    for i in range(4):
        if np.all(p[i] == "."):
            idxs.append(i)
    p = np.delete(p, idxs, 0)
    # 縦方向で.のみの列を削除
    idxs = []
    for i in range(4):
        if np.all(p[:, i] == "."):
            idxs.append(i)
    p = np.delete(p, idxs, 1)
    ps.append(p)

@lru_cache(maxsize=None)
def rotate_x(num):
    return np.rot90(ps[0], num)

@lru_cache(maxsize=None)
def rotate_y(num):
    return np.rot90(ps[1], num)

@lru_cache(maxsize=None)
def rotate_z(num):
    return np.rot90(ps[2], num)

@lru_cache(maxsize=None)
def out_of_range(x, y):
    return x < 0 or x > 3 or y < 0 or y > 3


# 全探索
# 3種
# 回転4パターン
# 座標位置12x12パターン？
for x_rotate in range(4):
    for y_rotate in range(4):
        z_rotate = 0
        for xx in range(4):
            for xy in range(4):
                for yx in range(4):
                    for yy in range(4):
                        for zx in range(4):
                            for zy in range(4):
                                x = rotate_x(x_rotate)
                                y = rotate_y(y_rotate)
                                z = rotate_z(z_rotate)
                                board = [["." for _ in range(10)] for _ in range(10)]
                                valid = True
                                # 書き込む
                                for i in range(x.shape[0]):
                                    for j in range(x.shape[1]):
                                        if x[i][j] == "#":
                                            if out_of_range(xx + i, xy + j):
                                                valid = False
                                                break
                                            board[xx + i][xy + j] = "#"
                                if not valid:
                                    continue
                                for i in range(y.shape[0]):
                                    for j in range(y.shape[1]):
                                        if y[i][j] == "#":
                                            if board[yx + i][yy + j] == "#":
                                                # 書き込み済み
                                                valid = False
                                                break
                                            if out_of_range(yx + i, yy + j):
                                                valid = False
                                                break
                                            board[yx + i][yy + j] = "#"
                                    if not valid:
                                        break
                                if not valid:
                                    continue
                                for i in range(z.shape[0]):
                                    for j in range(z.shape[1]):
                                        if z[i][j] == "#":
                                            if board[zx + i][zy + j] == "#":
                                                # 書き込み済み
                                                valid = False
                                                break
                                            if out_of_range(zx + i, zy + j):
                                                valid = False
                                                break
                                            board[zx + i][zy + j] = "#"
                                    if not valid:
                                        break
                                if not valid:
                                    continue
                                if valid:
                                    # 4x4の領域が埋まってるかチェック
                                    count = 0
                                    for i in range(4):
                                        for j in range(4):
                                            if board[i][j] == "#":
                                                count += 1
                                    if count == 16:
                                        print("Yes")
                                        exit()
print("No")

