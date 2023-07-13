import sys
input = lambda: sys.stdin.readline().rstrip()

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
base_a = a[:]

# 愚直にやると 2**1000 = 1024**100で間に合わない
# チェックでhw回のループを回すのでそれだけで10**6くらいかかる
# DPで解く
# dp[i][j] = i行目まで見た時に、それまでに孤立した状態を作らないようにした時の操作の最小数, jはiを反転したかどうかの2値

dp = [[float('inf')] * 2 for _ in range(h + 1)]
dp[0][0] = 0
dp[0][1] = 1

def swap(array):
    res = []
    for a_i in array:
        if a_i == 0:
            res.append(1)
        else:
            res.append(0)
    return res

def neighbor_check(a1, a2):
    # a1を孤立させないようにチェック
    pass
for i in range(1, h + 1):
    # i-1行目が反転している場合、そうでない場合、i行目を反転する場合、しない場合の4通り
    for j in range(2):
        for k in range(2):
            a_j = a[i - 1][:]
            a_k = a[i][:]
            if j == 1:
                a_j = swap(a_j)
            if k == 1:
                a_k = swap(a_k)


