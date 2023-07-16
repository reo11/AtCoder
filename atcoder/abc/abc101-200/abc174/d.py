from collections import deque

n = int(input())
c = list(input())

# WRはNG
# RWまたはR, Wにする
# RWの境界の候補がN - 1個

ans = [float("inf"), float("inf"), float("inf")]

# RW
r_idx = deque([])
w_idx = deque([])
for i in range(n):
    if c[i] == "R":
        r_idx.append(i)
    else:
        w_idx.append(i)

# all R
# 全てRにするのにかかるコストはlen(W)
ans[1] = len(w_idx)

# all W
# 全てWにするのにかかるコストはlen(R)
ans[2] = len(r_idx)

count = 0
# 最も右にあるRが最も左にあるWより左にある場合完了
# print(r_idx, w_idx)
while len(r_idx) > 0 and len(w_idx) > 0 and r_idx[-1] > w_idx[0]:
    # print(c)
    # 最も右にあるRを最も左にあるw_idxと入れ替える
    r_i = r_idx.pop()
    w_i = w_idx.popleft()
    tmp = c[r_i]
    c[r_i] = c[w_i]
    c[w_i] = tmp
    count += 1

ans[0] = count
# print(ans)
print(min(ans))
