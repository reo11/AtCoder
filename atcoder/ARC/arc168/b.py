from bisect import bisect_left, bisect_right
from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
xor_sum_memo = defaultdict(int)
# 大きい順に試す
a.sort()

INF = 10**16
for ai in a:
    xor_sum_memo[INF] ^= ai


def nim(k, pre_k=INF):
    # 更新分だけ追加計算
    # 更新範囲は [k + 1, pre_k]のai
    xor_sum = xor_sum_memo[pre_k]
    idx = bisect_left(a, k + 1)
    for i in range(idx, len(a)):

        if a[i] < k + 1:
            continue
        if a[i] > pre_k:
            break
        xor_sum ^= a[i]
        xor_sum ^= a[i] % (k + 1)
    xor_sum_memo[k] = xor_sum
    if xor_sum == 0:
        return -1
    else:
        return k


ans = []
pre_k = INF
k_candidates = []
for ai in a:
    for j in range(3):
        k = ai + j - 1
        k_candidates.append(k)
k_candidates = set(k_candidates)
k_candidates = sorted(list(k_candidates), reverse=True)
for k in k_candidates:
    res = nim(k, pre_k)
    if res != -1:
        ans.append(res)
    pre_k = k
    if len(ans) > 0:
        break
# print(ans)
# print(xor_sum_memo)
if len(ans) == 0:
    print(0)
elif max(ans) >= max(a):
    print(-1)
else:
    print(max(ans))
