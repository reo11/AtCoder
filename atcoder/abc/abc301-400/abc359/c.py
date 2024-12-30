sx, sy = map(int, input().split())
tx, ty = map(int, input().split())

# step1, 45度方向への移動は(dx + dy) // 2
# step2で45度移動終えた後の移動を計算

dx = tx - sx
dy = ty - sy

dist = min(abs(dx), abs(dy))
tmpx = sx + dist * (1 if dx > 0 else -1)
tmpy = sy + dist * (1 if dy > 0 else -1)

ans = 0

# step1
ans += dist

# step2
# tmpx, tmpyからtx, tyまでの移動
if tx - tmpx == 0:
    # 縦方向の移動のみの場合は単純
    ans += abs(ty - tmpy)
else:
    # 横方向の場合、スタート地点と終了地点のブロックによって変化する
    # yが偶数の場合、境目はmod2の1と0の間
    # yが奇数の場合、境目はmod2の0と1の間
    ans += abs(tx - tmpx) // 2
    if tmpy % 2 == 0:
        if tmpx % 2 == 1 and tx - tmpx > 0:
            ans += abs(tx - tmpx) % 2
        elif tmpx % 2 == 0 and tx - tmpx < 0:
            ans += abs(tx - tmpx) % 2
    else:
        if tmpx % 2 == 0 and tx - tmpx > 0:
            ans += abs(tx - tmpx) % 2
        elif tmpx % 2 == 1 and tx - tmpx < 0:
            ans += abs(tx - tmpx) % 2
print(ans)
