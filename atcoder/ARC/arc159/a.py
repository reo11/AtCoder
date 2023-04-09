import numpy as np
import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
st = []

ans = []
for _ in range(q):
    s, t = map(int, input().split())
    a[(s - 1) % n][(t - 1) % n]
    st.append([s, t])

# 距離行列の初期化
for i in range(n):
    for j in range(n):
        if a[i][j] == 0:
            a[i][j] = np.inf
a = np.array(a)
distance_matrix = a.copy()

# ワーシャルフロイド法による距離行列の計算
for k in range(len(distance_matrix)):
    for i in range(len(distance_matrix)):
        for j in range(len(distance_matrix)):
            distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])

for s, t in st:
    ans_i = distance_matrix[(s - 1) % n][(t - 1) % n]
    if ans_i < np.inf:
        ans.append(int(ans_i))
    else:
        ans.append(-1)
print("\n".join(list(map(str, ans))))
