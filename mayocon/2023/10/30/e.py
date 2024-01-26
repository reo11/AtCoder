# H <= 10に対してbit全探索を行なう
# 分割箇所は9個以下なので2**9 = 512通り
# W方向については貪欲に決めていけば最適
from collections import defaultdict

h, w, k = map(int, input().split())
s = [list(map(int, list(input()))) for _ in range(h)]
ans = float("inf")
for h_bit in range(2**h):
    cut = 0
    # i行目に対してグループ付け
    group = [0] * h
    group_num = 0
    for i in range(h):
        group[i] = group_num
        if (h_bit >> i) & 1:
            cut += 1
            group_num += 1
    # print(h_bit, group, cut)
    counter = defaultdict(lambda: 0)
    cut_flag = False
    valid_flag = True
    cut_history = []
    for i in range(w):
        for j in range(h):
            if s[j][i] == 1:
                counter[group[j]] += 1
                if counter[group[j]] > k:
                    # 超えたタイミングで1つ前でカットしたことにする
                    cut_flag = True
                    break
        if cut_flag:
            cut_flag = False
            cut += 1
            # cut_history.append(i)
            counter = defaultdict(lambda: 0)
            for j in range(h):
                if s[j][i] == 1:
                    counter[group[j]] += 1
                    if counter[group[j]] > k:
                        valid_flag = False
    if valid_flag:
        ans = min(ans, cut)
        # print(h_bit, ans, cut)
        # print(cut_history)
print(ans)
