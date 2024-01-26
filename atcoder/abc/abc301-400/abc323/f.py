INF = 10**18
xa, ya, xb, yb, xc, yc = map(int, input().split())
# 荷物から目的地の方向を求める
# 横方向から押すパターンと縦方向から押すパターンを考える


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


to_push = [yc - yb, xc - xb]  # [上に押す距離, 右に押す距離]

# print(to_push)

cost1 = 0
current_a_pos = [ya, xa]
# 横方向から押していくパターン
# 箱の右側に移動する最短コスト, ただし箱の座標は通過できない
if abs(to_push[1]) > 0:
    pos = [0, 0]
    if to_push[1] > 0:
        # 左が初期位置
        pos = [yb, xb - 1]
    elif to_push[1] < 0:
        pos = [yb, xb + 1]
    cost1 = manhattan_distance(xa, ya, pos[1], pos[0])
    # print(cost1, xa, ya, pos[1], pos[0])
    if ya == yb and ((to_push[1] < 0 and xa < xb) or (to_push[1] > 0 and xa > xb)):
        # マンハッタン距離+2コストが必要
        cost1 += 2
    current_a_pos = pos
    # 横移動させる
    cost1 += abs(to_push[1])

    if abs(to_push[0]) > 0:
        # 縦移動させる
        cost1 += abs(to_push[0]) + 2
    else:
        # 縦移動させる必要がない
        pass
else:
    # 横移動させる必要がない
    # 縦移動させる位置にそのままつく
    pos = [0, 0]
    if to_push[0] > 0:
        # 下が初期位置
        pos = [yb - 1, xb]
    elif to_push[0] < 0:
        pos = [yb + 1, xb]
    cost1 = manhattan_distance(xa, ya, pos[1], pos[0])
    # 初期位置に着くのに箱に干渉する場合
    if xa == xb and ((to_push[0] < 0 and xa < xb) or (to_push[0] > 0 and xa > xb)):
        # マンハッタン距離+2コストが必要
        cost1 += 2
    if abs(to_push[0]) > 0:
        # 縦移動させる
        cost1 += abs(to_push[0]) + 2
    else:
        # 縦移動させる必要がない
        pass

cost2 = 0
current_a_pos = [ya, xa]
# 縦方向から押していくパターン
if abs(to_push[0]) > 0:
    pos = [0, 0]
    if to_push[0] > 0:
        # 下が初期位置
        pos = [yb - 1, xb]
    elif to_push[0] < 0:
        pos = [yb + 1, xb]
    cost2 = manhattan_distance(xa, ya, pos[1], pos[0])
    # print(cost2)
    if xa == xb and ((to_push[0] < 0 and ya < yb) or (to_push[0] > 0 and ya > yb)):
        # マンハッタン距離+2コストが必要
        cost2 += 2
    current_a_pos = pos
    # 横移動させる
    cost2 += abs(to_push[0])

    if abs(to_push[1]) > 0:
        # 縦移動させる
        cost2 += abs(to_push[1]) + 2
    else:
        # 縦移動させる必要がない
        pass
else:
    pos = [0, 0]
    if to_push[1] > 0:
        # 下が初期位置
        pos = [yb, xb - 1]
    elif to_push[1] < 0:
        pos = [yb, xb + 1]
    cost2 = manhattan_distance(xa, ya, pos[1], pos[0])
    # 初期位置に着くのに箱に干渉する場合
    if ya == yb and ((to_push[1] < 0 and ya < yb) or (to_push[1] > 0 and ya > yb)):
        # マンハッタン距離+2コストが必要
        cost2 += 2
    if abs(to_push[1]) > 0:
        # 縦移動させる
        cost2 += abs(to_push[1]) + 2
    else:
        # 縦移動させる必要がない
        pass
# print(to_push)
# print(cost1, cost2)
print(min([cost1, cost2]))
