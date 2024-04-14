import numpy as np

a = [list(map(int, input().split())) for _ in range(3)]
a = np.array(a)

# 最善の行動をすると必ず引き分けになる
# 最終的に引き分けになる場合、反転、回転を同じとみなした場合、3パターンしかない
# 全パターンを試して、高橋くんが勝つパターンがあれば高橋くんの勝ち

patterns = [
    [
        [1, 1, 2],
        [2, 1, 1],
        [1, 2, 2]
    ],
    [
        [1, 1, 2],
        [2, 2, 1],
        [1, 1, 2]
    ],
    [
        [1, 1, 2],
        [2, 2, 1],
        [1, 2, 1]
    ]
]

def check(a, pattern):
    loop_count = 0
    takahashi_win_count = 0
    for rotate_degree in [0, 90, 180, 270]:
        a_rotated = np.rot90(a, rotate_degree)
        for filp_vertical in [False, True]:
            for filp_horizontal in [False, True]:
                a_copy = np.copy(a_rotated)
                if filp_vertical:
                    a_copy = np.flipud(a_copy)
                if filp_horizontal:
                    a_copy = np.fliplr(a_copy)
                takahashi = 0
                aoki = 0
                for i in range(3):
                    for j in range(3):
                        if pattern[i][j] == 1:
                            takahashi += a_copy[i][j]
                        else:
                            aoki += a_copy[i][j]
                loop_count += 1
                if takahashi > aoki:
                    takahashi_win_count += 1
    if pattern[1][1] == 1:
        if takahashi_win_count >= loop_count:
            return True
        else:
            return False
    else:
        if takahashi_win_count >= loop_count // 4:
            return True
        else:
            return False

ans = []
count = 0
for pattern in patterns:
    is_check_ok = check(a, pattern)
    ans.append(is_check_ok)

if ans[0] or (ans[1] and ans[2]):
    print("Takahashi")
else:
    print("Aoki")
