from collections import deque
n, x, y = map(int, input().split())
a = list(map(int, input().split()))

if n == 1:
    if a[0] == y:
        print("Yes")
        print("L")
        exit()
    elif -a[0] == y:
        print("Yes")
        print("R")
        exit()

def solve_half(ax, target_x):
    # 半分全列挙して可能かどうかを判定する
    # 不可能な場合は空行列
    # 可能な場合は正負のリストを返す（0: 負, 1: 正）
    halfs = [ax[:len(ax) // 2], ax[len(ax) // 2:]]
    values = [dict(), dict()]
    for i, half in enumerate(halfs):
        que = deque([[0, 0, 0]]) # [value, path]
        while que:
            value, depth, path = que.popleft()
            if depth == len(half):
                values[i][value] = path
            else:
                que.append([value + half[depth], depth + 1, path * 10 + 2])
                que.append([value - half[depth], depth + 1, path * 10 + 1])

    if len(values[0]) == 1:
        if target_x in values[1]:
            path = []
            for si in list(str(values[1][target_x])):
                if si == "2":
                    path.append(1)
                else:
                    path.append(0)
            return path
        else:
            return []

    for v, path1 in values[0].items():
        if target_x - v in values[1]:
            path2 = values[1][target_x - v]
            path = []
            # print(path1, path2)
            for si in list(str(path1)):
                if si == "2":
                    path.append(1)
                else:
                    path.append(0)
            for si in list(str(path2)):
                if si == "2":
                    path.append(1)
                else:
                    path.append(0)
            # print(path)
            return path
    return []

# 4分割して半分全列挙
def solve(a):
    ay = a[::2]
    ax = a[1::2]

    path_y = deque(solve_half(ay, y))
    path_x = deque(solve_half(ax, x))
    if not path_y or not path_x:
        print("No")
        return

    ans = []
    direction = 0 # 0: x正, 1: x負, 2: y正, 3: y負
    while path_y or path_x:
        if path_y:
            d = path_y.popleft()
            if d == 0:
                if direction == 0:
                    ans.append("R")
                else:
                    ans.append("L")
                direction = 3
            else:
                if direction == 0:
                    ans.append("L")
                else:
                    ans.append("R")
                direction = 2
        if path_x:
            d = path_x.popleft()
            if d == 0:
                if direction == 2:
                    ans.append("L")
                else:
                    ans.append("R")
                direction = 1
            else:
                if direction == 2:
                    ans.append("R")
                else:
                    ans.append("L")
                direction = 0
    print("Yes")
    print("".join(ans))
    return

solve(a)
# 奇数回目の操作でy方向に動く
# 偶数回目の操作でx方向に動く



